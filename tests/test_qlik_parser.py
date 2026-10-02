from app.domain.metrics.parsers.qlik import parse_qlik_metric


def test_parse_basic_qlik_metric():
    expression = "Sum({<Status={'Completed'}>} NetAmount)"

    result = parse_qlik_metric(expression)

    assert result.measure == "NetAmount"
    assert result.aggregation == "SUM"
    assert result.filters == [
        "Status = 'Completed'"
    ]
    assert result.parser == "qlik"
    assert result.parse_status == "complete"

def test_parse_simple_qlik_metric():
    expression = "Sum(NetAmount)"

    result = parse_qlik_metric(expression)

    assert result.measure == "NetAmount"
    assert result.aggregation == "SUM"
    assert result.filters == []