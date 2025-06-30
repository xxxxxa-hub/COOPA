import json
from pathlib import Path
from smolagents import LiteLLMModel, tool, CodeAgent
# from src.base_agent import CodeAgent
from smolagents.monitoring import LogLevel
from dotenv import load_dotenv
load_dotenv()

import os
import base64

# ✅ Set Langfuse OTEL environment variables
# LANGFUSE_PUBLIC_KEY = "pk-lf-fc94b01e-f660-4a4c-9604-4c99b27202d0"
# LANGFUSE_SECRET_KEY = "sk-lf-1f332ec0-da26-4536-98da-d46ea57f83c4"
# LANGFUSE_AUTH = base64.b64encode(f"{LANGFUSE_PUBLIC_KEY}:{LANGFUSE_SECRET_KEY}".encode()).decode()

# os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "https://cloud.langfuse.com/api/public/otel"
# os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Basic {LANGFUSE_AUTH}"
# os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN", "")

# # ✅ Setup OpenTelemetry tracing
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import SimpleSpanProcessor
# from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

# trace_provider = TracerProvider()
# trace_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter()))

# # ✅ Import your custom instrumentor
# from src.custom_smolagents_instrumentor import CustomSmolagentsInstrumentor
# from openinference.instrumentation import using_session

import argparse
import tempfile
import os
import shutil

from datetime import datetime
from .run import create_manager_agent

def get_current_timestamp():
    now = datetime.now()
    return now.strftime("%Y%m%d_%H%M%S")

def run_experiment(
    dataset_path,
    cur_date_time,
    model_id="gpt-4.1",
    knowledge_base_directory="apps/operations_research/or_knowledge_base",
    index_dir="apps/operations_research/or_vector_store",
    working_directory=None,
    output_path="experiment_results.jsonl"
):
    
    # CustomSmolagentsInstrumentor().instrument(tracer_provider=trace_provider)
    if "nlp4lp" in dataset_path:
        dataset_name = "nlp4lp"
    elif "nlp4opt" in dataset_path:
        dataset_name = "nlp4opt"
    elif "industryor" in dataset_path:
        dataset_name = "industryor"

    if working_directory is None:
        working_directory = tempfile.mkdtemp()
    
    manager_agent = create_manager_agent(
        model_id=model_id,
        knowledge_base_directory=knowledge_base_directory,
        index_dir=index_dir,
        working_directory=working_directory,
    )
    
    results = []
    with open(dataset_path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            question = item["question"]
            gold_answer = item["answer"]
            idx = item.get("index", None)
            # if int(idx) < 52:
            #     continue

            # session_id = f"{cur_date_time}_{dataset_name}_{idx}"

            # Clear the working directory for each new problem
            shutil.rmtree(working_directory)
            os.makedirs(working_directory, exist_ok=True)
            # with using_session(session_id=session_id):

                # Ask the agent to solve the problem
            prompt = f"Solve the following operations research problem:\n\n{question}\n\n You must return only the computed objective value (no explanation) as your final answer. Otherwise, the answer will be considered wrong."
            try:
                agent_response = manager_agent.run(prompt, reset=True)
                # Try to extract a number from the response
                import re
                match = re.search(r"[-+]?\d*\.\d+|\d+", str(agent_response))
                if match:
                    predicted = float(match.group())
                    correct = abs(predicted - float(gold_answer)) < 1e-4
                else:
                    predicted = None
                    correct = False
            # Handle any exceptions that occur during the agent's execution
            except Exception as e:
                agent_response = str(e)
                predicted = None
                correct = False

            result = {
                "index": idx,
                "question": question,
                "gold_answer": gold_answer,
                "predicted_answer": predicted,
                "agent_response": agent_response,
                "correct": correct,
            }
            print(f"Problem {idx}: Correct={correct} | Gold={gold_answer} | Predicted={predicted}")
            results.append(result)
            # Optionally, write results incrementally
            with open(output_path, "a", encoding="utf-8") as out_f:
                out_f.write(json.dumps(result) + "\n")
                
                # ask the manager agent to save any useful knowledge to the knowledge base with error handling
                # try:
                #     manager_agent.run("Please save any useful knowledge from this problem to the knowledge base. This is at your discretion and the purpose of the knowledge base is to help you solve future problems. Report the update you have made to the knowledge base as final answer", reset=False)
                # except Exception as e:
                #     print(f"Error saving knowledge to the knowledge base: {e}")
                #     continue

    print(f"Experiment finished. Results saved to {output_path}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run batch experiments with manager agent on the selected dataset.")
    parser.add_argument("--dataset", type=str, default="nlp4opt")
    parser.add_argument("--model_id", type=str, default="gpt-4.1")
    parser.add_argument("--knowledge_base_directory", type=str, default=None)
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    cur_date_time = get_current_timestamp()

    if args.knowledge_base_directory is None:
        args.knowledge_base_directory = f"apps/operations_research/or_knowledge_base_{args.dataset}"
    if args.output is None:
        args.output = f"apps/operations_research/datasets/{args.dataset}/experiment_results_{cur_date_time}.jsonl"

    index_dir = f"apps/operations_research/or_vector_store_{args.dataset}"

    run_experiment(
        dataset_path=f"apps/operations_research/datasets/{args.dataset}/{args.dataset}.jsonl",
        cur_date_time=cur_date_time,
        model_id=args.model_id,
        knowledge_base_directory=args.knowledge_base_directory,
        index_dir=index_dir,
        output_path=args.output,
    )