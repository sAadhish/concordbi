from app.domain.metrics.comparator import compare_metrics
from app.domain.metrics.models import NormalizedMetricDefinition


def test_equivalent_metrics():
    definition_a = NormalizedMetricDefinition(
        measure="net_amount",
        aggregation="SUM",
        filters=["status = 'completed'"],
        base_table="orders",
        parser="sqlglot",
    )

    definition_b = NormalizedMetricDefinition(
        measure="net_amount",
        aggregation="SUM",
        filters=["status = 'completed'"],
        base_table="orders",
        parser="sqlglot",
    )

    result = compare_metrics(
        metric_a_id="revenue_finance",
        definition_a=definition_a,
        metric_b_id="revenue_operations",
        definition_b=definition_b,
    )

    assert result.metric_a_id == "revenue_finance"
    assert result.metric_b_id == "revenue_operations"
    assert result.relationship == "equivalent"


def test_related_metrics_with_different_filters():
    definition_a = NormalizedMetricDefinition(
        measure="net_amount",
        aggregation="SUM",
        filters=["status = 'completed'"],
        base_table="orders",
        parser="sqlglot",
    )

    definition_b = NormalizedMetricDefinition(
        measure="net_amount",
        aggregation="SUM",
        filters=[
            "status = 'completed'",
            "is_test = false",
        ],
        base_table="orders",
        parser="sqlglot",
    )

    result = compare_metrics(
        metric_a_id="revenue_finance",
        definition_a=definition_a,
        metric_b_id="revenue_sales",
        definition_b=definition_b,
    )

    assert result.metric_a_id == "revenue_finance"
    assert result.metric_b_id == "revenue_sales"
    assert result.relationship == "related"


def test_unrelated_metrics_with_different_measures():
    definition_a = NormalizedMetricDefinition(
        measure="net_amount",
        aggregation="SUM",
        filters=["status = 'completed'"],
        base_table="orders",
        parser="sqlglot",
    )

    definition_b = NormalizedMetricDefinition(
        measure="customer_age",
        aggregation="AVG",
        filters=[],
        base_table="customers",
        parser="sqlglot",
    )

    result = compare_metrics(
        metric_a_id="revenue",
        definition_a=definition_a,
        metric_b_id="average_customer_age",
        definition_b=definition_b,
    )

    assert result.metric_a_id == "revenue"
    assert result.metric_b_id == "average_customer_age"
    assert result.relationship == "unrelated"