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
        "Conduct thorough reviews of the implemented code related to optimization problems. "
    )
    inputs = {}
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

    def forward(self) -> str:
        """
        Read code from solve.py, parameters from parameters.json, and problem from problem.txt,
        then send them to OpenAI's API for code review.
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

        # Combine all content
        full_content = "\n\n".join(content_parts)

        # Send to OpenAI API with instructor for structured output
        system_prompt = (
        "You are a lead Operations Research Scientist and technical reviewer. "
        "Your goal is to AUDIT optimization models (Pyomo/Gurobi/PuLP) for correctness, robustness, and logic. "
        "Do not focus on trivial style issues (like variable naming preferences) unless they cause ambiguity. "
        "Focus on MATHEMATICAL VALIDITY and BUSINESS LOGIC. "
        "\n\n"
        "CONDUCT YOUR REVIEW USING THIS HIERARCHICAL CHECKLIST:\n"
        "\n"
        "### TIER 1: SOLVER COMPATIBILITY & SYNTAX (The 'Will it run?' Check)\n"
        "1. **Linearity & Convexity**: \n"
        "   - Are non-linear functions (`abs`, `max`, `min`, `floor`, `if/else`) applied directly to decision variables? \n"
        "   - This is a CRITICAL FAIL for LP/MILP solvers. These logic must be modeled using binary variables or linear constraints.\n"
        "2. **Index Alignment & Bounds**: \n"
        "   - Check for Off-By-One errors (e.g., Python 0-index vs. Mathematical 1-index).\n"
        "   - Are loop boundaries correct? (e.g., `range(T)` vs `range(1, T+1)`).\n"
        "3. **Variable Domains**: \n"
        "   - Are discrete decisions (e.g., number of trucks, yes/no decisions) modeled as `Integers` or `Binary`?\n"
        "   - Are continuous quantities (e.g., money, water, time) modeled as `Reals`?\n"
        "\n"
        "### TIER 2: SYSTEM DYNAMICS & FLOW LOGIC (The 'Does it flow?' Check)\n"
        "4. **Flow Balance & Conservation Laws**: \n"
        "   - For any node/time-step: Does `Input + Previous_Storage == Output + Current_Storage`? \n"
        "   - Resources (money, inventory, time) cannot appear or disappear by magic. \n"
        "   - **FAIL** if specific time periods are modeled as isolated buckets without linking to previous/next periods.\n"
        "5. **State Transition Continuity**: \n"
        "   - Does the state at $t$ (e.g., inventory, location, fund balance) correctly depend on the state at $t-1$?\n"
        "   - Check distinct 'Before Action' vs 'After Action' states if simultaneous events occur.\n"
        "6. **Boundary Conditions**: \n"
        "   - Are initial conditions ($t=0$) properly constrained?\n"
        "   - Are end-of-horizon conditions ($t=T$) handled (e.g., minimum ending inventory)?\n"
        "\n"
        "### TIER 3: SEMANTIC & PHYSICAL REALITY (The 'Does it make sense?' Check)\n"
        "7. **Objective Function Alignment**: \n"
        "   - Does the minimization/maximization target represent the GLOBAL goal? \n"
        "   - Beware of minimizing a local variable (e.g., 'Cost in Jan') instead of the global variable (e.g., 'Total Initial Investment' or 'Sum of Costs').\n"
        "8. **Feasibility Buffers**: \n"
        "   - Can the constraints theoretically be met? \n"
        "\n"
        "RESPONSE GUIDELINES:\n"
        "- **Logic First**: If you find a logic flaw (Tier 2 or 3), prioritize it over syntax errors.\n"
        "- **Structural Fixes**: Do not just say 'Change variable X'. Say 'Refactor the constraint to track cumulative flow: S[t] = S[t-1] + ...'.\n"
        "- **Pass criteria**: Return `Pass=True` ONLY if the model accurately represents the physical/economic reality described in the problem text AND is mathematically solvable."
        )

        result = self.client.chat.completions.create(
            model=self.model_id,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": full_content}
            ],
            response_model=CodeReviewResult,
            temperature=1.0,
        )

        return f"Code Review Result:\nPass: {result.Pass}\nExplanation: {result.Explanation}"


def main():
    """Test the CodeReview tool with a specific working directory."""
    working_dir = "/hpc/group/fanglab/xx102/COOPA-main/working_directory/BWOR_openrouter-google-gemini-2.5-flash_v12_formulation_only/problem_0"

    # Create CodeReview instance
    code_reviewer = CodeReview(working_dir=working_dir, model_id="openrouter/google/gemini-2.5-flash")

    # Call forward() with no arguments
    print("Running code review...")
    print("-" * 80)

    try:
        result = code_reviewer.forward()
        print(result)
    except Exception as e:
        print(f"Error during code review: {e}")
        import traceback
        traceback.print_exc()

    print("-" * 80)
    print("Code review completed.")


if __name__ == "__main__":
    main()
