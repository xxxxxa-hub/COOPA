from smolagents.tools import Tool
import os
import json
from openai import OpenAI
from typing import Any
import importlib.util
from pydantic import BaseModel
from dotenv import load_dotenv
import instructor
from litellm import completion

load_dotenv()


class CodeReviewResult(BaseModel):
    """Structured output for code review."""
    Pass: bool
    Explanation: str


class CodeReview(Tool):
    name = "code_review"
    description = (
        "Review optimization code using the execution result or error log. "
        "Pass the execution output (stdout/stderr/traceback) as the execution_log argument."
    )
    inputs = {
        "execution_log": {
            "type": "string",
            "description": "The execution result or error log from running the solver code via load_object_from_python_file().",
        }
    }
    output_type = "string"

    def __init__(self, working_dir, model_id):
        super().__init__()
        self.working_dir = working_dir
        self.model_id = model_id
        # Patch OpenAI client with instructor for structured output
        # self.client = instructor.from_openai(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))
        if "openrouter" in model_id:
            self.client = instructor.from_litellm(completion, mode=instructor.Mode.OPENROUTER_STRUCTURED_OUTPUTS)
        else:
            self.client = instructor.from_litellm(completion, mode=instructor.Mode.MD_JSON)

    def forward(self, execution_log: str) -> str:
        """
        Read code from solve.py, parameters from parameters.json, and problem from problem.txt,
        along with the execution log from running the solver, then send them to the LLM for review.
        Returns a string with Pass status and explanation.
        """
        # Read the files
        solve_py_path = os.path.join(self.working_dir, "solve.py")
        parameters_path = os.path.join(self.working_dir, "parameters.json")
        problem_path = os.path.join(self.working_dir, "problem.txt")

        # Initialize content parts
        content_parts = []

        # Read solve.py
        if os.path.exists(solve_py_path):
            with open(solve_py_path, 'r') as f:
                solve_code = f.read()
                content_parts.append(f"## Solve Code (solve.py):\n\n```python\n{solve_code}\n```")
        else:
            content_parts.append("## Solve Code: File not found (solve.py)")

        # Read parameters.json
        if os.path.exists(parameters_path):
            with open(parameters_path, 'r') as f:
                parameters = json.load(f)
                content_parts.append(f"## Parameters (parameters.json):\n\n```json\n{json.dumps(parameters, indent=2)}\n```")
        else:
            content_parts.append("## Parameters: File not found (parameters.json)")

        # Read problem.txt
        if os.path.exists(problem_path):
            with open(problem_path, 'r') as f:
                problem_content = f.read()
                content_parts.append(f"## Problem Description (problem.txt):\n\n{problem_content}")
        else:
            content_parts.append("## Problem Description: File not found (problem.txt)")

        # Add execution log
        content_parts.append(f"## Execution Log:\n\n```\n{execution_log}\n```")

        # Combine all content
        full_content = "\n\n".join(content_parts)

        # Send to OpenAI API with instructor for structured output
        system_prompt = (
        "You are a lead Operations Research Scientist and technical reviewer. "
        "Your goal is to AUDIT optimization models (Pyomo/Gurobi/PuLP) for correctness, robustness, and logic. "
        "You will be given the source code, parameters, problem description, AND the execution log "
        "(which may contain solver output, tracebacks, or error messages). "
        "Do not focus on trivial style issues (like variable naming preferences) unless they cause ambiguity. "
        "Focus on MATHEMATICAL VALIDITY, BUSINESS LOGIC, and EXECUTION CORRECTNESS. "
        "\n\n"
        "=== CRITICAL REVIEW PRINCIPLES ===\n"
        "Before reviewing, internalize these principles:\n"
        "\n"
        "1. **DEMONSTRATE, don't speculate.** Only return Pass=False if you can point to a CONCRETE, "
        "PROVABLE error — a specific constraint that is wrong, a term missing from the objective, "
        "a parameter used incorrectly, or a result that demonstrably violates a stated requirement. "
        "Do NOT fail a model based on speculation like 'this might be wrong' or 'this could potentially lead to issues.'\n"
        "\n"
        "2. **Equivalent formulations are valid.** Multiple mathematically equivalent formulations exist for the same problem. "
        "If the current formulation produces the correct feasible region and objective, it is correct — even if you would "
        "have formulated it differently. For example, aggregate flow conservation (Total_A = Total_B) is equivalent to "
        "per-route flow tracking when costs are per-machine, not per-route. Do NOT reject a valid formulation just because "
        "an alternative formulation exists.\n"
        "\n"
        "3. **Actionable fixes only.** If you identify a real error and return Pass=False, your explanation MUST include "
        "a SPECIFIC, UNAMBIGUOUS fix — the exact constraint to change, the exact term to add/remove, or the exact code line "
        "to modify. Do NOT suggest vague reformulations like 'use Cash_start and Cash_end variables' without specifying "
        "the exact mathematical expressions. A bad fix suggestion is worse than no suggestion.\n"
        "\n"
        "CONDUCT YOUR REVIEW USING THIS HIERARCHICAL CHECKLIST:\n"
        "\n"
        "### TIER 0: EXECUTION RESULT ANALYSIS (The 'Did it run correctly?' Check)\n"
        "0. **Execution Errors**: \n"
        "   - If the execution log contains a traceback or error, identify the root cause (e.g., import errors, NameError, TypeError, solver failures). \n"
        "   - Provide a specific fix for the error. \n"
        "   - This is the HIGHEST PRIORITY. If the code crashed, focus on fixing the crash first.\n"
        "1. **Solver Status**: \n"
        "   - Did the solver return 'optimal'? If 'infeasible' or 'unbounded', diagnose which constraints or bounds are likely causing the issue.\n"
        "2. **Result Sanity Check**: \n"
        "   - Are the returned variable values and objective value reasonable given the problem description? \n"
        "   - Do the results violate any obvious physical or business constraints (e.g., negative quantities, values exceeding capacity)?\n"
        "\n"
        "### TIER 1: SOLVER COMPATIBILITY & SYNTAX (The 'Will it run?' Check)\n"
        "3. **Linearity & Convexity**: \n"
        "   - Are non-linear functions (`abs`, `max`, `min`, `floor`, `if/else`) applied directly to decision variables? \n"
        "   - This is a CRITICAL FAIL for LP/MILP solvers. These logic must be modeled using binary variables or linear constraints.\n"
        "4. **Index Alignment & Bounds**: \n"
        "   - Check for Off-By-One errors (e.g., Python 0-index vs. Mathematical 1-index).\n"
        "   - Are loop boundaries correct? (e.g., `range(T)` vs `range(1, T+1)`).\n"
        "5. **Variable Domains**: \n"
        "   - Are discrete decisions (e.g., number of trucks, yes/no decisions) modeled as `Integers` or `Binary`?\n"
        "   - Are continuous quantities (e.g., money, water, time) modeled as `Reals`?\n"
        "\n"
        "### TIER 2: MODEL FORMULATION CORRECTNESS (The 'Does the model match the problem?' Check)\n"
        "6. **Objective Function Alignment**: \n"
        "   - Does the objective direction (minimize/maximize) match the problem goal? \n"
        "   - Does the objective expression include ALL relevant cost/revenue/penalty terms described in the problem? \n"
        "   - Are any terms missing, duplicated, or have the wrong sign?\n"
        "7. **Constraint Coverage**: \n"
        "   - Is every requirement stated in the problem description represented by at least one constraint in the model? \n"
        "   - List any problem requirements that have NO corresponding constraint.\n"
        "8. **Flow Balance & Conservation Laws**: \n"
        "   - For any node/time-step: Does `Input + Previous_Storage == Output + Current_Storage`? \n"
        "   - Resources (money, inventory, time) cannot appear or disappear. \n"
        "   - **FAIL** only if you can show a SPECIFIC scenario where resources are created or destroyed by the model.\n"
        "9. **State Transition Continuity**: \n"
        "   - Does the state at $t$ (e.g., inventory, location, fund balance) correctly depend on the state at $t-1$?\n"
        "   - Are initial conditions ($t=0$) and end-of-horizon conditions ($t=T$) properly constrained?\n"
        "10. **Parameter Usage**: \n"
        "   - Are the correct parameter values from parameters.json used in the correct places? \n"
        "   - Are any parameters swapped, inverted, or applied to the wrong variables?\n"
        "\n"
        "RESPONSE GUIDELINES:\n"
        "- **Execution Errors First**: If the execution log shows a crash or traceback, diagnose and fix that before anything else.\n"
        "- **Model Logic Second**: If execution succeeded, verify the model formulation matches the problem description.\n"
        "- **Be specific**: Do not just say 'the timing is wrong'. Say exactly which constraint has the wrong expression and what it should be.\n"
        "- **One issue at a time**: If you find multiple issues, focus on the MOST CRITICAL one and provide a clear fix for it.\n"
        "- **Pass criteria**: Return `Pass=True` if the execution succeeded with an optimal solution AND the model correctly "
        "represents the problem described in the problem text (correct objective, all constraints present, correct parameter usage). "
        "Return `Pass=False` ONLY if you can identify a SPECIFIC, DEMONSTRABLE error in the model formulation."
        )

        result = self.client.chat.completions.create(
            model=self.model_id,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": full_content}
            ],
            response_model=CodeReviewResult,
            temperature=0.2,
        )

        return f"Code Review Result:\nPass: {result.Pass}\nExplanation: {result.Explanation}"


def main():
    """Test the CodeReview tool with a specific working directory."""
    working_dir = "/hpc/group/fanglab/xx102/COOPA-main/working_directory/BWOR_openrouter-google-gemini-2.5-flash_v12_formulation_only/problem_0"

    # Create CodeReview instance
    code_reviewer = CodeReview(working_dir=working_dir, model_id="openrouter/google/gemini-2.5-flash")

    # Call forward() with a sample execution log
    sample_log = "Status: optimal\nObjective: 100.0\nVariables:\n  x = 10.0\n  y = 5.0"
    print("Running code review...")
    print("-" * 80)

    try:
        result = code_reviewer.forward(execution_log=sample_log)
        print(result)
    except Exception as e:
        print(f"Error during code review: {e}")
        import traceback
        traceback.print_exc()

    print("-" * 80)
    print("Code review completed.")


if __name__ == "__main__":
    main()
