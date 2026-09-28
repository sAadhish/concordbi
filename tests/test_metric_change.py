from app.domain.metrics.models import MetricChange

def test_metric_change():
    version=MetricChange(
        change_id="change_001",
    metric_id="revenue_finance",
    from_version_id="revenue_finance_v1",
    to_version_id="revenue_finance_v2",
    change_type="definition_changed",
    )
    assert version.change_id == "change_001"
    assert version.metric_id == "revenue_finance"
    assert version.from_version_id == "revenue_finance_v1"
    assert version.to_version_id == "revenue_finance_v2"
    assert version.change_type == "definition_changed"



