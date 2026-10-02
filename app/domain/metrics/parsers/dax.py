import re

from app.domain.metrics.models import NormalizedMetricDefinition


def parse_dax_metric(dax: str) -> NormalizedMetricDefinition:
    expression = dax.strip()

    match = re.search(
        r"SUM\s*\(\s*([A-Za-z_][\w]*)\[([A-Za-z_][\w]*)\]\s*\)",
        expression,
        re.IGNORECASE,
    )

    if not match:
        raise ValueError("Unsupported DAX metric expression")

    table = match.group(1)
    column = match.group(2)

    filters = []

    filter_matches = re.findall(
        r"([A-Za-z_][\w]*)\[([A-Za-z_][\w]*)\]\s*=\s*[\"']([^\"']+)[\"']",
        expression,
        re.IGNORECASE,
    )

    for filter_table, filter_column, value in filter_matches:
        filters.append(
            f"{filter_table}[{filter_column}] = '{value}'"
        )

    return NormalizedMetricDefinition(
        measure=f"{table}[{column}]",
        aggregation="SUM",
        filters=filters,
        base_table=table,
        parser="dax",
    )