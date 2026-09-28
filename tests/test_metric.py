from app.domain.metrics.models import MetricDefinition
import pytest
from pydantic import ValidationError

def test_create_revenue_metric():
    metric = MetricDefinition(
        metric_id="revenue_finance_v1",
        name="Revenue",
        source_asset="finance_dashboard",
        source_type="dashboard",
        measure="net_amount",
        aggregation="SUM",
        filters=[
            "status = 'completed'",
            "is_test = false",
        ],
        base_table="orders",
        grain="monthly",
        definition="""
            SELECT SUM(net_amount)
            FROM orders
            WHERE status = 'completed'
            AND is_test = false
        """,
        definition_language="sql",
        description="Monthly revenue from completed non-test orders.",
    )

    assert metric.metric_id == "revenue_finance_v1"
    assert metric.name == "Revenue"
    assert metric.measure == "net_amount"
    assert metric.aggregation == "SUM"
    assert metric.base_table == "orders"
    assert metric.grain == "monthly"

        ### Active Customers

def test_metric_with_optional_fields():
    metric = MetricDefinition(
        metric_id="active_customers_v1",
        name="Active Customers",
        source_asset="sales_dashboard",
        source_type="dashboard",
        definition="COUNT(DISTINCT customer_id)",
        definition_language="sql",
    )

    assert metric.metric_id == "active_customers_v1"
    assert metric.name == "Active Customers"
    assert metric.measure is None
    assert metric.aggregation is None
    assert metric.filters == []
    assert metric.joins == []


## Pydantic’s validation

def test_metric_requires_required_fields():
    with pytest.raises(ValidationError):
        MetricDefinition(
            name="Revenue",
            source_asset="finance_dashboard",
            source_type="dashboard",
            definition="SUM(net_amount)",
        )



def test_metric_serialization():
    metric = MetricDefinition(
        metric_id="revenue_finance_v1",
        name="Revenue",
        source_asset="finance_dashboard",
        source_type="dashboard",
        measure="net_amount",
        aggregation="SUM",
        filters=["status = 'completed'"],
        base_table="orders",
        grain="monthly",
        definition="SUM(net_amount)",
        definition_language="sql",
    )

    print(metric.model_dump())