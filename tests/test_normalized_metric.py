from app.domain.metrics.models import NormalizedMetricDefinition


def test_create_normalized_metric_definition():
    metric = NormalizedMetricDefinition(
        measure="net_amount",
        aggregation="SUM",
        filters=["status = 'completed'"],
        base_table="orders",
        parser="test",
    )

    assert metric.measure == "net_amount"
    assert metric.aggregation == "SUM"
    assert metric.filters == ["status = 'completed'"]
    assert metric.base_table == "orders"
    assert metric.joins == []
    assert metric.grain is None
    assert metric.parser == "test"
    assert metric.parse_status == "complete"