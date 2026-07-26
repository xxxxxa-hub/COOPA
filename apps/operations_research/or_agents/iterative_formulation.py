"""
Iterative formulation refinement with confidence evaluation.

This module provides functionality to:
1. Extract an initial formulation from a problem
2. Evaluate confidence in the formulation
3. Refine the formulation based on confidence feedback
4. Iterate until the formulation meets confidence thresholds
"""

from __future__ import annotations

import json
import os
from typing import Dict, Any, Optional, Tuple
from litellm import completion
import instructor

from .formulation import (
    OptimizationFormulation,
    FormulationEvaluation,
    create_instructor_client,
    extract_formulation,
)


def format_formulation_for_evaluation(formulation: OptimizationFormulation) -> str:
    """
    Convert an OptimizationFormulation object into a formatted string for evaluation.

    Args:
        formulation: The structured optimization formulation

    Returns:
        A formatted string representation of the formulation
    """
    parts = []

    # Parameters section
    if formulation.parameters:
        parts.append("## PARAMETERS:")
        for param in formulation.parameters:
            param_str = f"- {param.name} ({param.data_type}): {param.description}"
            if param.value is not None:
                param_str += f" = {param.value}"
            if param.units:
                param_str += f" [{param.units}]"
            parts.append(param_str)
            parts.append(f'  Evidence: "{param.source.quote}"')
            if param.source.note:
                parts.append(f"  Evidence note: {param.source.note}")

    # Variables section
    if formulation.variables:
        parts.append("\n## DECISION VARIABLES:")
        for var in formulation.variables:
            var_str = f"- {var.name} ({var.data_type}): {var.description}"
            var_str += f" | Domain: {var.domain}"
            parts.append(var_str)
            parts.append(f'  Evidence: "{var.source.quote}"')
            if var.source.note:
                parts.append(f"  Evidence note: {var.source.note}")

    # Objective section
    parts.append("\n## OBJECTIVE:")
    parts.append(f"- Sense: {formulation.objective.sense.upper()}")
    parts.append(f"- Description: {formulation.objective.description}")
    parts.append(f"- Expression: {formulation.objective.expression}")
    parts.append(f"- Variables involved: {', '.join(formulation.objective.variables_involved)}")
    parts.append(f'- Evidence: "{formulation.objective.source.quote}"')
    if formulation.objective.source.note:
        parts.append(f"- Evidence note: {formulation.objective.source.note}")

    # Constraints section
    if formulation.constraints:
        parts.append("\n## CONSTRAINTS:")
        for i, constraint in enumerate(formulation.constraints, 1):
            parts.append(f"\n{i}. {constraint.name} ({constraint.sense}):")
            parts.append(f"   Expression: {constraint.expression}")
            parts.append(f"   Variables: {', '.join(constraint.variables_involved)}")
            parts.append(f'   Evidence: "{constraint.source.quote}"')
            if constraint.source.note:
                parts.append(f"   Evidence note: {constraint.source.note}")

    return "\n".join(parts)


def apply_evidence_consistency_penalties(
    evaluation: FormulationEvaluation,
) -> FormulationEvaluation:
    """Apply deterministic score caps for unsupported or ambiguous modeling choices."""
    components = (
        evaluation.parameters,
        evaluation.decision_variables,
        evaluation.objective,
        evaluation.constraints,
    )
    unsupported = []
    ambiguities = []
    for component in components:
        unsupported.extend(component.unsupported_assumptions)
        ambiguities.extend(component.ambiguities)
        if component.unsupported_assumptions:
            component.confidence = min(component.confidence, 70)

    if unsupported:
        evaluation.evidence_consistency = min(evaluation.evidence_consistency, 60)
        evaluation.has_unresolved_issues = True
    elif ambiguities:
        evaluation.evidence_consistency = min(evaluation.evidence_consistency, 80)
        evaluation.has_unresolved_issues = True

    component_min = min(component.confidence for component in components)
    evaluation.overall_confidence = min(
        evaluation.overall_confidence,
        component_min,
        evaluation.evidence_consistency,
    )
    if evaluation.overall_confidence < 80:
        evaluation.has_unresolved_issues = True
    return evaluation


def formulation_selection_key(entry: Dict[str, Any], history_index: int) -> tuple:
    """Rank candidates by grounded weakest-link quality, then raw quality and recency."""
    evaluation = entry["evaluation"]
    return (
        min(entry["min_confidence"], evaluation.evidence_consistency),
        not evaluation.has_unresolved_issues,
        evaluation.evidence_consistency,
        entry["overall_confidence"],
        history_index,
    )


def evaluate_formulation_confidence(
    raw_question: str,
    formulation: OptimizationFormulation,
    client=None,
    model: str = "gpt-4o"
) -> FormulationEvaluation:
    """
    Evaluate confidence scores for each component of the formulation.

    Args:
        raw_question: The original optimization problem question
        formulation: The structured formulation to evaluate
        client: Instructor client (if None, creates a new one)
        model: Model to use for evaluation (supports all LiteLLM models)

    Returns:
        FormulationEvaluation object with confidence scores and explanations
    """
    # Format formulation for evaluation
    formulation_str = format_formulation_for_evaluation(formulation)

    # Create evaluation prompt
    evaluation_prompt = f"""You are an expert in optimization and mathematical modeling. Your task is to evaluate the quality, correctness, and consistency with the source question of an optimization problem formulation.

Given:
1. **Raw Question**: {raw_question}

2. **Proposed Formulation**:
{formulation_str}

Please evaluate the confidence (0-100) for each of the following components:

1. **PARAMETERS**: Are all necessary parameters identified with correct values and units?
2. **DECISION VARIABLES**: Are all decision variables properly defined with correct domains?
3. **OBJECTIVE**: Is the objective function correct and does it properly represent what should be optimized?
4. **CONSTRAINTS**: Are all necessary constraints included and correctly formulated?

For each component, provide a confidence score from 0-100 and a brief explanation.

SOURCE-CONSISTENCY RULES:
- Treat the raw question as authoritative. A plausible or conventional modeling choice is
  not evidence.
- Check that each displayed Evidence quote actually supports the full modeling choice,
  rather than merely mentioning the same entity.
- Compare every material semantic choice in the formulation against the raw question.
  Do not accept information that was added, strengthened, or reinterpreted without
  textual support.
- Put every unsupported choice in that component's `unsupported_assumptions`. Put
  unresolved wording with multiple defensible interpretations in `ambiguities`.
- An unsupported assumption must cap that component at 70 or below. Ambiguity must not
  be silently resolved by choosing whichever interpretation seems convenient.
- Set `evidence_consistency` to reflect source support across the whole formulation
  and set `has_unresolved_issues=true` if any unsupported assumption or material ambiguity
  remains. Explain the concrete issue in `overall_assessment`.
"""

    # Use LiteLLM for all models via instructor
    if client is None:
        client = instructor.from_litellm(completion)

    # Set parameters for Qwen model
    kwargs = {}
    if any(x in model for x in ["gemini"]): # "thinking"
        kwargs.update({"extra_body":{"reasoning": {"effort": "high"}}})
    elif any(x in model for x in ["o3", "o4", "gpt-5"]):
        kwargs.update({"reasoning_effort": "high"})

    evaluation = client.chat.completions.create(
        model=model,
        response_model=FormulationEvaluation,
        messages=[
            {"role": "user", "content": evaluation_prompt}
        ],
        **kwargs
    )

    return apply_evidence_consistency_penalties(evaluation)


def refine_formulation(
    raw_question: str,
    current_formulation: OptimizationFormulation,
    confidence_evaluation: FormulationEvaluation,
    client,
    model: str = "gpt-4o-mini",
    formulation_history: Optional[list] = None
) -> OptimizationFormulation:
    """
    Refine a formulation based on confidence evaluation feedback.

    Args:
        raw_question: The original problem text
        current_formulation: The current formulation to refine
        confidence_evaluation: The confidence evaluation results
        client: Instructor client for extraction
        model: Model to use for refinement
        formulation_history: List of all previous formulations with their evaluations

    Returns:
        Refined OptimizationFormulation
    """
    # Build history section if available
    history_section = ""
    if formulation_history:
        history_section = "\n\n**HISTORY OF PREVIOUS FORMULATIONS:**\n"
        for entry in formulation_history:
            iteration = entry['iteration']
            past_formulation = entry['formulation']
            past_evaluation = entry['evaluation']

            past_formulation_str = format_formulation_for_evaluation(past_formulation)
            history_section += f"\n--- Iteration {iteration} ---\n"
            history_section += f"Formulation:\n{past_formulation_str}\n\n"
            history_section += f"Confidence Scores:\n"
            history_section += f"- Parameters: {past_evaluation.parameters.confidence}/100 - {past_evaluation.parameters.explanation}\n"
            history_section += f"- Decision Variables: {past_evaluation.decision_variables.confidence}/100 - {past_evaluation.decision_variables.explanation}\n"
            history_section += f"- Objective: {past_evaluation.objective.confidence}/100 - {past_evaluation.objective.explanation}\n"
            history_section += f"- Constraints: {past_evaluation.constraints.confidence}/100 - {past_evaluation.constraints.explanation}\n"
            history_section += f"- Evidence consistency: {past_evaluation.evidence_consistency}/100\n"
            history_section += f"- Has unresolved issues: {past_evaluation.has_unresolved_issues}\n"
            for component_name, component in (
                ("Parameters", past_evaluation.parameters),
                ("Decision Variables", past_evaluation.decision_variables),
                ("Objective", past_evaluation.objective),
                ("Constraints", past_evaluation.constraints),
            ):
                if component.unsupported_assumptions:
                    history_section += (
                        f"- Unsupported assumptions ({component_name}): "
                        + "; ".join(component.unsupported_assumptions)
                        + "\n"
                    )
                if component.ambiguities:
                    history_section += (
                        f"- Ambiguities ({component_name}): "
                        + "; ".join(component.ambiguities)
                        + "\n"
                    )

    # Create refinement prompt
    refinement_prompt = f"""You are refining an optimization formulation. Review all previous attempts and the feedback to create a better formulation.

**Original Problem:**
{raw_question}
{history_section}

Please create a REFINED formulation that addresses all the identified issues from past iterations. Learn from what worked well in previous iterations and avoid repeating mistakes. Pay special attention to the components with lower confidence scores. Ensure that:
1. All parameters are correctly identified and valued
2. All decision variables are properly defined with correct domains
3. The objective function correctly represents what needs to be optimized
4. All necessary constraints are included and correctly formulated
5. Every material modeling choice is supported by the original problem. Do not add,
   strengthen, or reinterpret requirements using unstated conventions.
6. If the wording is ambiguous, preserve that uncertainty in the relevant source note
   instead of silently choosing a stronger interpretation.

Provide the complete refined formulation."""

    # Use instructor to extract refined formulation
    from openai.types.chat import ChatCompletionMessageParam
    from .formulation import SYSTEM_PROMPT

    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": SYSTEM_PROMPT.strip()},
        {"role": "user", "content": refinement_prompt},
    ]

    # Set parameters for Qwen model
    kwargs = {}
    if any(x in model for x in ["gemini"]): # "thinking"
        kwargs.update({"extra_body":{"reasoning": {"effort": "high"}}})
    elif any(x in model for x in ["o3", "o4", "gpt-5"]):
        kwargs.update({"reasoning_effort": "high"})

    refined_formulation = client.chat.completions.create(
        model=model,
        response_model=OptimizationFormulation,
        messages=messages,
        **kwargs
    )

    return refined_formulation


def extract_formulation_with_refinement(
    problem_text: str,
    max_iterations: int = 3,
    formulation_model: str = "gpt-4o-mini",
    evaluation_model: str = "gpt-4o",
    api_key: Optional[str] = None,
    verbose: bool = True
) -> Tuple[OptimizationFormulation, FormulationEvaluation, int]:
    """
    Extract and iteratively refine a formulation.

    This function tracks ALL formulations generated during iteration and
    returns the one with the HIGHEST minimum confidence score across all
    components (max-min criterion). This ensures the selected formulation
    has the most balanced quality with no weak components.

    Args:
        problem_text: The original optimization problem text
        max_iterations: Maximum number of refinement iterations
        formulation_model: Model to use for formulation extraction/refinement
        evaluation_model: Model to use for confidence evaluation
        api_key: OpenAI API key (if None, uses OPENAI_API_KEY env variable)
        verbose: Whether to print progress information

    Returns:
        Tuple of (best_formulation, best_evaluation, best_iteration_number)
        where best_evaluation is a FormulationEvaluation object with confidence
        scores and the formulation is the one with the highest minimum confidence
        score across all components
    """
    # Create instructor client for formulation with the specified model
    formulation_client = create_instructor_client(
        model_name=formulation_model,
        timeout=120.0
    )

    # Extract initial formulation
    if verbose:
        print("Extracting initial formulation...")

    formulation = extract_formulation(
        problem_text=problem_text,
        client=formulation_client,
        model=formulation_model
    )

    # Track all formulations and their evaluations
    formulation_history = []

    # Iterative refinement loop
    for iteration in range(1, max_iterations + 1):
        if verbose:
            print(f"\n{'=' * 80}")
            print(f"ITERATION {iteration}/{max_iterations}")
            print('=' * 80)
            print()
            print("Current Formulation:")
            print("-" * 80)
            print(format_formulation_for_evaluation(formulation))
            print("-" * 80)
            print()
            print("Evaluating confidence...")

        # Evaluate confidence
        evaluation = evaluate_formulation_confidence(
            raw_question=problem_text,
            formulation=formulation,
            client=formulation_client,
            model=evaluation_model
        )

        overall_confidence = evaluation.overall_confidence

        # Get individual component confidences
        params_confidence = evaluation.parameters.confidence
        vars_confidence = evaluation.decision_variables.confidence
        obj_confidence = evaluation.objective.confidence
        constraints_confidence = evaluation.constraints.confidence

        # Calculate min confidence (weakest component)
        min_confidence = min(
            params_confidence,
            vars_confidence,
            obj_confidence,
            constraints_confidence,
            evaluation.evidence_consistency,
        )

        # Store this formulation in history
        formulation_history.append({
            'iteration': iteration,
            'formulation': formulation,
            'evaluation': evaluation,
            'overall_confidence': overall_confidence,
            'min_confidence': min_confidence
        })

        if verbose:
            print()
            print("Confidence Scores:")
            print(f"  Overall: {overall_confidence}/100")
            print(f"  Min (weakest component): {min_confidence}/100")
            print(f"  Evidence consistency: {evaluation.evidence_consistency}/100")
            print(f"  Has unresolved issues: {evaluation.has_unresolved_issues}")
            print(f"  - Parameters: {params_confidence}/100")
            print(f"    {evaluation.parameters.explanation}")
            print(f"  - Decision Variables: {vars_confidence}/100")
            print(f"    {evaluation.decision_variables.explanation}")
            print(f"  - Objective: {obj_confidence}/100")
            print(f"    {evaluation.objective.explanation}")
            print(f"  - Constraints: {constraints_confidence}/100")
            print(f"    {evaluation.constraints.explanation}")
            print()

        # If this is the last iteration, we'll select the best from history
        if iteration == max_iterations:
            break

        # Refine formulation
        if verbose:
            print(f"Refining formulation based on feedback...")

        try:
            formulation = refine_formulation(
                raw_question=problem_text,
                current_formulation=formulation,
                confidence_evaluation=evaluation,
                client=formulation_client,
                model=formulation_model,
                formulation_history=formulation_history
            )
            if verbose:
                print("✓ Refinement complete")
        except Exception as e:
            if verbose:
                print(f"✗ Refinement failed: {e}")
                print(f"Selecting best formulation from history...")
            # Don't return immediately, break to select best from history
            break

    # Select the best formulation from history based on:
    # 1. Highest source-consistent weakest-component confidence
    # 2. Prefer candidates without unresolved issues
    # 3. Highest evidence consistency and overall confidence
    # 4. Latest iteration when otherwise tied
    if not formulation_history:
        raise ValueError("No formulations were evaluated")

    best_idx = max(
        range(len(formulation_history)),
        key=lambda i: formulation_selection_key(formulation_history[i], i)
    )
    best_entry = formulation_history[best_idx]

    if verbose:
        print(f"\n{'=' * 80}")
        print("SELECTING BEST FORMULATION FROM HISTORY")
        print("Criteria: Source-consistent min score, unresolved status, consistency, overall, recency")
        print('=' * 80)
        print(f"\nEvaluated {len(formulation_history)} formulation(s) across {best_entry['iteration']} iteration(s)")
        print("\nConfidence scores by iteration:")
        for entry in formulation_history:
            marker = " ← SELECTED" if entry == best_entry else ""
            print(f"  Iteration {entry['iteration']}: "
                  f"Min={entry['min_confidence']}/100, "
                  f"EvidenceConsistency={entry['evaluation'].evidence_consistency}/100, "
                  f"Unresolved={entry['evaluation'].has_unresolved_issues}, "
                  f"Overall={entry['overall_confidence']}/100{marker}")
        if best_entry["evaluation"].has_unresolved_issues:
            print("\nNOTICE: The selected candidate contains unresolved issues. "
                  "The automated pipeline will continue and retain this status for analysis.")
        print(f"\nReturning formulation from iteration {best_entry['iteration']} "
              f"with min confidence {best_entry['min_confidence']}/100 "
              f"(overall: {best_entry['overall_confidence']}/100)")

    return best_entry['formulation'], best_entry['evaluation'], best_entry['iteration']
