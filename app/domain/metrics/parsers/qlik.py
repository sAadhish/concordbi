import re

from app.domain.metrics.models import NormalizedMetricDefinition


def parse_qlik_metric(expression: str) -> NormalizedMetricDefinition:
    expression = expression.strip()

    match = re.search(
        r"(?i)\bSUM\s*\(\s*(?:\{<(?P<set_analysis>.*?)>\}\s*)?(?P<measure>[A-Za-z_][\w]*)\s*\)",
        expression,
    )

    if not match:
        raise ValueError("Unsupported Qlik metric expression")

    measure = match.group("measure")
    set_analysis = match.group("set_analysis")

    filters = []

    if set_analysis:
        filter_matches = re.findall(
            r"([A-Za-z_][\w]*)\s*=\s*\{([^}]*)\}",
            set_analysis,
        )

        for field, values in filter_matches:
            for value in values.split(","):
                value = value.strip().strip("'\"")

                filters.append(
                    f"{field} = '{value}'"
                )

    return NormalizedMetricDefinition(
        measure=measure,
        aggregation="SUM",
        filters=filters,
        parser="qlik",
    )