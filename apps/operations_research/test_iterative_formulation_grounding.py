from apps.operations_research.or_agents.formulation import (
    ComponentConfidence,
    ConstraintDefinition,
    FormulationEvaluation,
    ObjectiveDefinition,
    OptimizationFormulation,
    SourceReference,
    VariableDefinition,
)
from apps.operations_research.or_agents.iterative_formulation import (
    apply_evidence_consistency_penalties,
    format_formulation_for_evaluation,
    formulation_selection_key,
)


def _component(score=95, unsupported=None, ambiguities=None):
    return ComponentConfidence(
        confidence=score,
        explanation="test",
        unsupported_assumptions=unsupported or [],
        ambiguities=ambiguities or [],
    )


def _evaluation(score=95, unsupported=None, ambiguities=None):
    return FormulationEvaluation(
        parameters=_component(score),
        decision_variables=_component(score, unsupported, ambiguities),
        objective=_component(score),
        constraints=_component(score),
        overall_confidence=score,
        overall_assessment="test",
        evidence_consistency=score,
    )


def test_formatter_keeps_evidence_visible_to_evaluator():
    formulation = OptimizationFormulation(
        question="Produce at most two units.",
        parameters=[],
        variables=[
            VariableDefinition(
                name="x",
                data_type="continuous",
                description="production",
                domain="x >= 0",
                source=SourceReference(quote="Produce at most two units."),
            )
        ],
        objective=ObjectiveDefinition(
            sense="maximize",
            description="production",
            expression="x",
            variables_involved=["x"],
            source=SourceReference(quote="Produce"),
        ),
        constraints=[
            ConstraintDefinition(
                name="capacity",
                sense="<=",
                expression="x <= 2",
                variables_involved=["x"],
                source=SourceReference(quote="at most two units"),
            )
        ],
    )

    rendered = format_formulation_for_evaluation(formulation)

    assert 'Evidence: "Produce at most two units."' in rendered
    assert 'Evidence: "at most two units"' in rendered


def test_unsupported_assumption_is_deterministically_capped_and_flagged():
    evaluation = _evaluation(
        score=98,
        unsupported=["Integer domain is not stated in the question."],
    )

    result = apply_evidence_consistency_penalties(evaluation)

    assert result.decision_variables.confidence == 70
    assert result.evidence_consistency == 60
    assert result.overall_confidence == 60
    assert result.has_unresolved_issues is True


def test_selection_prefers_grounded_candidate_over_higher_raw_scores():
    unsupported = _evaluation(
        score=99,
        unsupported=["Changed 'at most two' to exactly two."],
    )
    apply_evidence_consistency_penalties(unsupported)
    grounded = _evaluation(score=85)
    entries = [
        {
            "evaluation": unsupported,
            "min_confidence": 70,
            "overall_confidence": unsupported.overall_confidence,
        },
        {
            "evaluation": grounded,
            "min_confidence": 85,
            "overall_confidence": grounded.overall_confidence,
        },
    ]

    best = max(range(len(entries)), key=lambda i: formulation_selection_key(entries[i], i))

    assert best == 1


def test_material_ambiguity_is_flagged_without_calling_it_unsupported():
    evaluation = _evaluation(
        score=95,
        ambiguities=["The surcharge timing is not specified."],
    )

    result = apply_evidence_consistency_penalties(evaluation)

    assert result.decision_variables.confidence == 95
    assert result.evidence_consistency == 80
    assert result.overall_confidence == 80
    assert result.has_unresolved_issues is True


def test_low_confidence_candidate_is_never_returned_as_unflagged():
    evaluation = _evaluation(score=72)

    result = apply_evidence_consistency_penalties(evaluation)

    assert result.overall_confidence == 72
    assert result.has_unresolved_issues is True
