"""Focused semantic-risk audit for iterative formulation confidence evaluation."""

from __future__ import annotations

import json
from typing import Literal, Optional

from pydantic import BaseModel

from .formulation import OptimizationFormulation


class SourceAuditIssue(BaseModel):
    issue_type: Literal[
        "contradiction",
        "unsupported_strengthening",
        "material_ambiguity",
        "missing_identifying_information",
    ]
    affected_dimension: Literal[
        "parameters", "decision_variables", "objective", "constraints", "overall"
    ]
    element_name: str
    source_quote: str
    formulation_claim: str
    alternative_interpretation: Optional[str] = None
    why_material: str


class SourceAuditResult(BaseModel):
    """At most one issue is surfaced to keep confidence evaluation focused."""

    flagged_issue: Optional[SourceAuditIssue] = None


class SourceAuditVerification(BaseModel):
    keep_issue: bool
    rationale: str
    counterfactual_impact: str


SCAN_SYSTEM_PROMPT = """You are a high-precision semantic-risk auditor for an optimization formulation.

Try to falsify the formulation's semantic interpretation by comparing it with the raw
question and element-level source quotes. Return at most one issue: the single clearest,
most consequential problem. Return null when there is no high-confidence issue.

Allowed issue types:
- contradiction: a claim conflicts with the question;
- unsupported_strengthening: a claim materially narrows the feasible set beyond the
  question;
- material_ambiguity: two ordinary, textually defensible interpretations exist, the
  formulation chooses one, and the alternatives can change the answer;
- missing_identifying_information: information needed for a unique requested numerical
  answer is absent from the complete question.

Evaluate support against the complete raw question, not the local quote in isolation. A
broad or incomplete local quote is not a reason to flag an otherwise source-consistent
element. For material_ambiguity, state the alternative interpretation and why both
readings are supported.

Do not flag equivalent mathematical encodings, ordinary task implications, hypothetical
real-world features absent from the closed-world question, or alternatives that cannot
change the requested answer. Be conservative. Never invent source text. Return JSON only."""


VERIFY_SYSTEM_PROMPT = """You are the precision verifier for a semantic-risk audit.

Decide whether the proposed issue should actually be shown to a confidence evaluator.
Keep it only when it survives the complete question, is not an equivalent encoding or
ordinary implication, is not implied by other constraints or redundant at every optimum,
and can plausibly change the feasible optimum, objective value, or uniquely requested
numerical answer.

For ambiguity, both interpretations must remain textually defensible after using all
numbers and context. For missing information, reject the issue if the information is
supplied or derivable elsewhere. Be conservative and do not find a new issue. Return JSON
only."""


def _model_kwargs(model: str) -> dict:
    if "gemini" in model:
        return {"extra_body": {"reasoning": {"effort": "high"}}}
    if any(name in model for name in ("o3", "o4", "gpt-5")):
        return {"reasoning_effort": "high"}
    return {}


def _audit_payload(
    raw_question: str,
    formulation: OptimizationFormulation,
) -> dict:
    elements: list[dict[str, str]] = []
    for parameter in formulation.parameters:
        elements.append(
            {
                "element_type": "parameter",
                "element_name": parameter.name,
                "formulation_claim": (
                    f"{parameter.description}; value={parameter.value}; units={parameter.units}"
                ),
                "source_quote": parameter.source.quote,
            }
        )
    for variable in formulation.variables:
        elements.append(
            {
                "element_type": "decision_variable",
                "element_name": variable.name,
                "formulation_claim": (
                    f"{variable.description}; type={variable.data_type}; "
                    f"domain={variable.domain}"
                ),
                "source_quote": variable.source.quote,
            }
        )
    elements.append(
        {
            "element_type": "objective",
            "element_name": "objective",
            "formulation_claim": (
                f"{formulation.objective.sense}: {formulation.objective.expression}; "
                f"{formulation.objective.description}"
            ),
            "source_quote": formulation.objective.source.quote,
        }
    )
    for constraint in formulation.constraints:
        elements.append(
            {
                "element_type": "constraint",
                "element_name": constraint.name,
                "formulation_claim": (
                    f"{constraint.expression}; sense={constraint.sense}"
                ),
                "source_quote": constraint.source.quote,
            }
        )
    return {"raw_question": raw_question, "formulation_elements": elements}


def scan_and_verify_source_issue(
    raw_question: str,
    formulation: OptimizationFormulation,
    client,
    model: str,
) -> tuple[SourceAuditResult, Optional[SourceAuditVerification]]:
    """Return one verified issue or no issue; audit failure must not alter main behavior."""

    kwargs = _model_kwargs(model)
    audit = client.chat.completions.create(
        model=model,
        response_model=SourceAuditResult,
        messages=[
            {"role": "system", "content": SCAN_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": json.dumps(
                    _audit_payload(raw_question, formulation),
                    ensure_ascii=False,
                ),
            },
        ],
        **kwargs,
    )
    if audit.flagged_issue is None:
        return audit, None

    verification = client.chat.completions.create(
        model=model,
        response_model=SourceAuditVerification,
        messages=[
            {"role": "system", "content": VERIFY_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": json.dumps(
                    {
                        "question_and_formulation": _audit_payload(
                            raw_question,
                            formulation,
                        ),
                        "proposed_issue": audit.flagged_issue.model_dump(),
                    },
                    ensure_ascii=False,
                ),
            },
        ],
        **kwargs,
    )
    if not verification.keep_issue:
        audit.flagged_issue = None
    return audit, verification


def format_verified_source_issue(audit: SourceAuditResult) -> str:
    issue = audit.flagged_issue
    if issue is None:
        return ""
    alternative = (
        f"\n- Alternative interpretation: {issue.alternative_interpretation}"
        if issue.alternative_interpretation
        else ""
    )
    return f"""

SOURCE AUDIT: POTENTIALLY PROBLEMATIC ELEMENT

The source scanner and a separate materiality verifier identified the following element
for focused review. This remains an audit lead, not an established error. Independently
verify it against the raw question before assigning confidence.

- Issue type: {issue.issue_type}
- Affected dimension: {issue.affected_dimension}
- Element: {issue.element_name}
- Formulation claim: {issue.formulation_claim}
- Source quote: {issue.source_quote}{alternative}
- Why it may affect the answer: {issue.why_material}
"""
