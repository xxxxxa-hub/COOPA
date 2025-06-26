#!/usr/bin/env python3
"""
Batch runner for Operations Research Agent with dataset questions.
This script automates the process of running the OR agent with questions from JSONL dataset files.
"""

import json
import argparse
import time
import os
from pathlib import Path
from datetime import datetime
import tempfile
import re
from typing import List, Dict, Any, Union

from .run import create_manager_agent


def load_jsonl_dataset(dataset_path: str) -> List[Dict[str, Any]]:
    """
    Load questions from a JSONL dataset file.
    
    Args:
        dataset_path: Path to the JSONL dataset file
        
    Returns:
        List of question dictionaries
    """
    questions = []
    with open(dataset_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if line:
                try:
                    question_data = json.loads(line)
                    questions.append(question_data)
                except json.JSONDecodeError as e:
                    print(f"Warning: Failed to parse line {line_num}: {e}")
                    continue
    return questions


def save_results(results: List[Dict[str, Any]], output_file: str):
    """
    Save results to a JSONL file.
    
    Args:
        results: List of result dictionaries
        output_file: Path to output file
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(json.dumps(result, ensure_ascii=False) + '\n')


def run_batch_questions(agent, questions: List[Dict[str, Any]], 
                       start_index: int = 0, end_index: int = None,
                       save_interval: int = 5) -> List[Dict[str, Any]]:
    """
    Run the agent on a batch of questions.
    
    Args:
        agent: The manager agent instance
        questions: List of question dictionaries
        start_index: Starting index (0-based)
        end_index: Ending index (exclusive), None for all questions
        save_interval: Save results every N questions
        
    Returns:
        List of results
    """
    if end_index is None:
        end_index = len(questions)
    
    results = []
    
    for i in range(start_index, min(end_index, len(questions))):
        question_data = questions[i]
        question_text = question_data.get('question', '')
        
        print(f"\n{'='*60}")
        print(f"Processing Question {i+1}/{len(questions)} (Index: {question_data.get('index', i+1)})")
        print(f"{'='*60}")
        print(f"Question: {question_text[:100]}{'...' if len(question_text) > 100 else ''}")
        print(f"Expected Answer: {question_data.get('answer', 'N/A')}")
        print(f"Origin: {question_data.get('ori', 'N/A')}")
        
        start_time = time.time()
        
        try:
            # Run the agent with just the raw question text
            # The agent already has all necessary prompts configured through prompt templates
            print("\nRunning agent...")
            response = agent.run(question_text, reset=True)
            
            end_time = time.time()
            processing_time = end_time - start_time
            
            # Extract objective value using LLM
            objective_value = extract_objective_value_with_llm(
                response, 
                question_text, 
                question_data.get('answer')
            )
            
            # Store result
            result = {
                'question_index': question_data.get('index', i+1),
                'original_question': question_text,
                'expected_answer': question_data.get('answer'),
                'origin': question_data.get('ori'),
                'agent_response': response,
                'objective_value': objective_value,
                'processing_time_seconds': processing_time,
                'timestamp': datetime.now().isoformat(),
                'status': 'completed'
            }
            
            results.append(result)
            
            print(f"\nCompleted in {processing_time:.2f} seconds")
            print(f"Agent response length: {len(str(response))} characters")
            if objective_value is not None:
                print(f"Extracted objective value: {objective_value}")
                if question_data.get('answer') is not None:
                    expected = question_data.get('answer')
                    print(f"Expected answer: {expected}")
                    if isinstance(expected, (int, float)) and isinstance(objective_value, (int, float)):
                        diff = abs(float(objective_value) - float(expected))
                        rel_error = diff / abs(float(expected)) if expected != 0 else float('inf')
                        print(f"Absolute difference: {diff:.2f}, Relative error: {rel_error:.2%}")
            else:
                print("No objective value could be extracted from response")
            
        except Exception as e:
            error_time = time.time() - start_time
            print(f"\nError processing question {i+1}: {str(e)}")
            
            result = {
                'question_index': question_data.get('index', i+1),
                'original_question': question_text,
                'expected_answer': question_data.get('answer'),
                'origin': question_data.get('ori'),
                'agent_response': None,
                'objective_value': None,
                'error': str(e),
                'processing_time_seconds': error_time,
                'timestamp': datetime.now().isoformat(),
                'status': 'error'
            }
            
            results.append(result)
        
        # Save intermediate results
        if (i + 1) % save_interval == 0:
            print(f"\nSaving intermediate results after {i + 1} questions...")
            temp_output = f"temp_results_up_to_{i+1}.jsonl"
            save_results(results, temp_output)
    
    return results


def extract_objective_value_with_llm(response_data: Any, question: str, expected_answer: Any = None) -> Union[float, int, None]:
    """
    Extract the objective value from the agent's response using a small LLM.
    
    Args:
        response_data: The agent's response (can be dict, string, or other format)
        question: The original question text for context
        expected_answer: The expected answer for reference (optional)
        
    Returns:
        The extracted objective value as a number, or None if not found
    """
    try:
        from litellm import completion
        
        # Convert response to string for analysis
        if isinstance(response_data, dict):
            response_text = json.dumps(response_data, indent=2)
        else:
            response_text = str(response_data)
        
        # Create a prompt for the small LLM to extract the objective value
        extraction_prompt = f"""You are tasked with extracting the numerical objective value from an operations research problem solution.

QUESTION: {question}

SOLUTION RESPONSE: {response_text}

Your task is to identify the single numerical value that represents the answer to the optimization problem (e.g., minimum cost, maximum profit, minimum number of items, etc.).

Look for values that represent:
- Minimum/maximum objective values
- Optimal costs, profits, or quantities being optimized
- The primary answer to the question being asked

Respond with ONLY the numerical value (integer or decimal). If you cannot find a clear objective value, respond with "NONE".

Examples:
- If the solution shows "minimum_total_wagons": 67, respond: 67
- If the solution shows "Maximum profit": 12000, respond: 12000
- If the solution shows "total_flowers": 400, respond: 400

Numerical value:"""

        # Use a small, fast model for extraction
        response = completion(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": extraction_prompt}],
            temperature=0,
            max_tokens=50
        )
        
        extracted_text = response.choices[0].message.content.strip()
        
        # Try to parse the extracted value
        if extracted_text.upper() == "NONE":
            return None
            
        # Remove any extra text and extract just the number
        number_match = re.search(r'([+-]?\d+(?:\.\d+)?)', extracted_text)
        if number_match:
            value_str = number_match.group(1)
            if '.' in value_str:
                return float(value_str)
            else:
                return int(value_str)
        
        return None
        
    except Exception as e:
        print(f"Warning: LLM extraction failed: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Batch run Operations Research Agent with dataset questions")
    
    parser.add_argument(
        "--dataset_path",
        default="apps/operations_research/datasets/nlp4lp/nlp4lp.jsonl",
        help="Path to the JSONL dataset file"
    )
    
    parser.add_argument(
        "--output",
        default=None,
        help="Output file for results (default: auto-generated based on dataset name and timestamp)"
    )
    
    parser.add_argument(
        "--model_id",
        default="gpt-4.1",
        help="Model ID to use for the agent (default: gpt-4.1)"
    )
    
    parser.add_argument(
        "--start_index",
        type=int,
        default=0,
        help="Start processing from this question index (0-based, default: 0)"
    )
    
    parser.add_argument(
        "--end_index",
        type=int,
        default=None,
        help="Stop processing at this question index (exclusive, default: process all)"
    )
    
    parser.add_argument(
        "--working_directory",
        default=None,
        help="Working directory for the agent (default: temporary directory)"
    )
    
    parser.add_argument(
        "--knowledge_base_directory",
        default="apps/operations_research/or_knowledge_base",
        help="Knowledge base directory (default: temporary directory)"
    )
    
    parser.add_argument(
        "--index_dir",
        default=None,
        help="Vector store index directory (default: temporary directory)"
    )
    
    parser.add_argument(
        "--save_interval",
        type=int,
        default=5,
        help="Save intermediate results every N questions (default: 5)"
    )
    
    args = parser.parse_args()
    
    # Validate dataset path
    if not os.path.exists(args.dataset_path):
        print(f"Error: Dataset file not found: {args.dataset_path}")
        return 1
    
    # Load dataset
    print(f"Loading dataset from: {args.dataset_path}")
    questions = load_jsonl_dataset(args.dataset_path)
    print(f"Loaded {len(questions)} questions")
    
    if len(questions) == 0:
        print("Error: No valid questions found in dataset")
        return 1
    
    # Validate indices
    if args.start_index < 0 or args.start_index >= len(questions):
        print(f"Error: start_index {args.start_index} is out of range [0, {len(questions)-1}]")
        return 1
    
    if args.end_index is not None and (args.end_index <= args.start_index or args.end_index > len(questions)):
        print(f"Error: end_index {args.end_index} is invalid (must be > {args.start_index} and <= {len(questions)})")
        return 1
    
    # Setup directories
    base_temp_dir = "apps/operations_research/temp_files"
    Path(base_temp_dir).mkdir(parents=True, exist_ok=True)
    
    if args.working_directory is None:
        args.working_directory = tempfile.mkdtemp(dir=base_temp_dir, prefix="batch_working_")
    
    if args.knowledge_base_directory is None:
        args.knowledge_base_directory = tempfile.mkdtemp(dir=base_temp_dir, prefix="batch_kb_")
    
    if args.index_dir is None:
        args.index_dir = tempfile.mkdtemp(dir=base_temp_dir, prefix="batch_index_")
    
    # Create output filename if not provided
    if args.output is None:
        dataset_name = Path(args.dataset_path).stem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        range_suffix = f"_{args.start_index}-{args.end_index or len(questions)}"
        args.output = f"batch_results_{dataset_name}{range_suffix}_{timestamp}.jsonl"
    
    print(f"\nConfiguration:")
    print(f"  Dataset: {args.dataset_path}")
    print(f"  Questions to process: {args.start_index} to {args.end_index or len(questions)} ({(args.end_index or len(questions)) - args.start_index} questions)")
    print(f"  Model: {args.model_id}")
    print(f"  Output file: {args.output}")
    print(f"  Working directory: {args.working_directory}")
    print(f"  Knowledge base: {args.knowledge_base_directory}")
    print(f"  Index directory: {args.index_dir}")
    print(f"  Save interval: {args.save_interval}")
    
    # Create the agent
    print(f"\nCreating manager agent...")
    try:
        manager_agent = create_manager_agent(
            model_id=args.model_id,
            knowledge_base_directory=args.knowledge_base_directory,
            index_dir=args.index_dir,
            working_directory=args.working_directory
        )
        print("Agent created successfully!")
    except Exception as e:
        print(f"Error creating agent: {e}")
        return 1
    
    # Run batch processing
    print(f"\nStarting batch processing...")
    start_time = time.time()
    
    try:
        results = run_batch_questions(
            manager_agent,
            questions,
            args.start_index,
            args.end_index,
            args.save_interval
        )
        
        total_time = time.time() - start_time
        
        # Save final results
        print(f"\nSaving final results to: {args.output}")
        save_results(results, args.output)
        
        # Print summary
        successful = len([r for r in results if r['status'] == 'completed'])
        failed = len([r for r in results if r['status'] == 'error'])
        
        print(f"\n{'='*60}")
        print(f"BATCH PROCESSING COMPLETE")
        print(f"{'='*60}")
        print(f"Total questions processed: {len(results)}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Total time: {total_time:.2f} seconds")
        print(f"Average time per question: {total_time/len(results):.2f} seconds")
        print(f"Results saved to: {args.output}")
        
        if failed > 0:
            print(f"\nFailed questions:")
            for result in results:
                if result['status'] == 'error':
                    print(f"  Question {result['question_index']}: {result.get('error', 'Unknown error')}")
        
        return 0
        
    except KeyboardInterrupt:
        print(f"\nBatch processing interrupted by user")
        # Save partial results
        if 'results' in locals() and results:
            interrupted_output = f"interrupted_{args.output}"
            print(f"Saving partial results to: {interrupted_output}")
            save_results(results, interrupted_output)
        return 1
    
    except Exception as e:
        print(f"\nUnexpected error during batch processing: {e}")
        return 1


if __name__ == "__main__":
    exit(main()) 