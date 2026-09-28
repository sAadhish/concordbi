from app.domain.metrics.models import MetricChange,MetricVersion

def detect_change(
        previous: MetricVersion,
        current: MetricVersion) -> MetricChange | None:

    if previous.definition == current.definition:
        return None
    
    return MetricChange(
        change_id=f"{previous.version_id}_to_{current.version_id}",
        metric_id=current.metric_id,
        from_version_id=previous.version_id,
        to_version_id=current.version_id,
        change_type="definition_changed",
    )


    