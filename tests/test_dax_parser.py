from app.domain.metrics.parsers.dax import parse_dax_metric


def test_parse_basic_dax_metric():
    dax = """
        Revenue =
        CALCULATE(
            SUM(Orders[NetAmount]),
            Orders[Status] = "Completed"
        )
    """

    result = parse_dax_metric(dax)

    assert result.measure == "Orders[NetAmount]"
    assert result.aggregation == "SUM"
    assert result.base_table == "Orders"
    assert result.filters == [
        "Orders[Status] = 'Completed'"
    ]
    assert result.parser == "dax"
    assert result.parse_status == "complete"


def test_parse_simple_dax_metric():
    dax = "Revenue = SUM(Orders[NetAmount])"

    result = parse_dax_metric(dax)

    assert result.measure == "Orders[NetAmount]"
    assert result.aggregation == "SUM"
    assert result.base_table == "Orders"
    assert result.filters == []