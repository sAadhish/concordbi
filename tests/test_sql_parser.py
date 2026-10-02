from app.domain.metrics.parsers.sql import parse_sql_metric


def test_parse_basic_sql_metric():
    sql = """
        SELECT SUM(net_amount)
        FROM orders
        WHERE status = 'completed'
    """

    result = parse_sql_metric(sql)

    assert result.measure == "net_amount"
    assert result.aggregation == "SUM"
    assert result.base_table == "orders"
    assert result.filters == ["status = 'completed'"]
    assert result.parser == "sqlglot"
    assert result.parse_status == "complete"


def test_parse_average_metric():
    sql = """
        SELECT AVG(order_value)
        FROM orders
    """

    result = parse_sql_metric(sql)

    assert result.measure == "order_value"
    assert result.aggregation == "AVG"
    assert result.base_table == "orders"
    assert result.filters == []


def test_parse_count_metric():
    sql = """
        SELECT COUNT(customer_id)
        FROM customers
        WHERE active = true
    """

    result = parse_sql_metric(sql)

    assert result.measure == "customer_id"
    assert result.aggregation == "COUNT"
    assert result.base_table == "customers"
    assert result.filters == ["active = TRUE"]