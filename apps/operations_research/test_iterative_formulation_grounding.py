from apps.operations_research.or_agents.iterative_formulation import (
    format_formulation_for_evaluation,
)
from apps.operations_research.or_agents.formulation import (
    ConstraintDefinition,
    ObjectiveDefinition,
    OptimizationFormulation,
    SourceReference,
    VariableDefinition,
)
from apps.operations_research.or_agents.source_audit import (
    SourceAuditIssue,
    SourceAuditResult,
    format_verified_source_issue,
)


def _formulation() -> OptimizationFormulation:
    source = SourceReference(quote="Production cannot exceed 10 units.")
    return OptimizationFormulation(
        question="Production cannot exceed 10 units. Maximize production.",
        parameters=[],
        variables=[
            VariableDefinition(
                name="x",
                data_type="integer",
                description="units produced",
                domain="x >= 0",
                source=source,
            )
        ],
        objective=ObjectiveDefinition(
            sense="maximize",
            description="maximize production",
            expression="x",
            variables_involved=["x"],
            source=SourceReference(quote="Maximize production."),
        ),
        constraints=[
            ConstraintDefinition(
                name="capacity",
                sense="<=",
                expression="x <= 10",
                variables_involved=["x"],
                source=source,
            )
        ],
    )


def test_main_branch_formatter_does_not_dump_all_source_quotes():
    formatted = format_formulation_for_evaluation(_formulation())

    assert "x <= 10" in formatted
    assert "Evidence:" not in formatted
    assert "Production cannot exceed 10 units." not in formatted


def test_empty_audit_adds_no_confidence_context():
    assert format_verified_source_issue(SourceAuditResult()) == ""


def test_verified_audit_context_contains_only_one_focused_issue():
    audit = SourceAuditResult(
        flagged_issue=SourceAuditIssue(
            issue_type="unsupported_strengthening",
            affected_dimension="constraints",
            element_name="capacity",
            formulation_claim="x = 10",
            source_quote="Production cannot exceed 10 units.",
            why_material="Equality removes feasible production levels below 10.",
        )
    )

    context = format_verified_source_issue(audit)

    assert "unsupported_strengthening" in context
    assert "x = 10" in context
    assert "Production cannot exceed 10 units." in context
    assert "Equality removes feasible production levels below 10." in context
