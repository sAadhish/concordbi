from datetime import datetime, timezone

from app.domain.metrics.models import MetricVersion


def test_create_metric_version():
    version = MetricVersion(
        version_id="revenue_finance_v1",
        metric_id="revenue_finance",
        snapshot_id="snapshot_2026_09_20",
        definition="SUM(net_amount) WHERE status = 'completed'",
        created_at=datetime.now(timezone.utc),
    )

    assert version.version_id == "revenue_finance_v1"
    assert version.metric_id == "revenue_finance"
    assert version.snapshot_id == "snapshot_2026_09_20"



