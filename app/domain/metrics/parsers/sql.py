import sqlglot
from sqlglot import exp

from app.domain.metrics.models import NormalizedMetricDefinition


def parse_sql_metric(sql: str) -> NormalizedMetricDefinition:
    tree = sqlglot.parse_one(sql)

    aggregate = tree.find(exp.AggFunc)

    if aggregate is None:
        raise ValueError("No aggregation found in SQL metric")

    if not isinstance(aggregate, exp.AggFunc):
        raise ValueError("Unsupported aggregation")

    aggregation = aggregate.key.upper()

    column = aggregate.find(exp.Column)

    if column is None:
        raise ValueError("No measure column found")

    measure = column.sql()

    table = tree.find(exp.Table)

    base_table = table.name if table else None

    filters = []

    where = tree.find(exp.Where)

    if where is not None:
        filters.append(where.this.sql())

    return NormalizedMetricDefinition(
        measure=measure,
        aggregation=aggregation,
        filters=filters,
        base_table=base_table,
        parser="sqlglot",
    )