from app.domain.metrics.models import NormalizedMetricDefinition
from app.domain.metrics.relationship import MetricRelationship


def compare_metrics(
    metric_a_id: str,
    definition_a: NormalizedMetricDefinition,
    metric_b_id: str,
    definition_b: NormalizedMetricDefinition,
) -> MetricRelationship:

    if (
        definition_a.measure == definition_b.measure
        and definition_a.aggregation == definition_b.aggregation
        and definition_a.filters == definition_b.filters
        and definition_a.base_table == definition_b.base_table
    ):
        relationship = "equivalent"

    elif definition_a.measure != definition_b.measure:
        relationship = "unrelated"

    else:
        relationship = "related"

    return MetricRelationship(
        metric_a_id=metric_a_id,
        metric_b_id=metric_b_id,
        relationship=relationship,
    )