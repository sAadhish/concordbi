from app.domain.metrics.models import MetricVersion
from  app.domain.metrics.change_detector import detect_change
from datetime import datetime, timezone


def test_detect_definition_change():
    previous = MetricVersion(
        version_id="revenue_v1",
        metric_id="revenue",
        snapshot_id="snapshot_1",
        definition="SUM(net_amount)",
        created_at=datetime(2026, 9, 20, tzinfo=timezone.utc),
    )

    current = MetricVersion(
        version_id="revenue_v2",
        metric_id="revenue",
        snapshot_id="snapshot_2",
        definition="SUM(gross_amount)",
        created_at=datetime(2026, 9, 21, tzinfo=timezone.utc),
    )

    change = detect_change(previous, current)

    assert change is not None
    assert change.metric_id == "revenue"
    assert change.from_version_id == "revenue_v1"
    assert change.to_version_id == "revenue_v2"
    assert change.change_type == "definition_changed"


def test_no_change_when_definition_is_same():
    previous = MetricVersion(
        version_id="revenue_v1",
        metric_id="revenue",
        snapshot_id="snapshot_1",
        definition="SUM(net_amount)",
        created_at=datetime(2026, 9, 20, tzinfo=timezone.utc),
    )

    current = MetricVersion(
        version_id="revenue_v2",
        metric_id="revenue",
        snapshot_id="snapshot_2",
        definition="SUM(net_amount)",
        created_at=datetime(2026, 9, 21, tzinfo=timezone.utc),
    )

    change = detect_change(previous, current)

    assert change is None