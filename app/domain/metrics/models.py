from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class MetricChange(BaseModel):
    change_id: str
    metric_id: str
    from_version_id: str
    to_version_id: str
    change_type: str

class MetricDefinition(BaseModel):
    metric_id: str
    name: str
    source_asset: str
    source_type: str
    measure: Optional[str] = None
    aggregation: Optional[str] = None
    filters: List[str] = Field(default_factory=list)
    base_table: Optional[str] = None
    joins: List[str] = Field(default_factory=list)
    grain: Optional[str] = None
    definition: str
    definition_language: Optional[str] = None
    description: Optional[str] = None


class MetricVersion(BaseModel):
    version_id: str
    metric_id: str
    snapshot_id: str
    definition: str
    created_at: datetime