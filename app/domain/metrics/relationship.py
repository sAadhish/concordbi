from typing import Literal

from pydantic import BaseModel


RelationshipType = Literal[
    "equivalent",
    "related",
    "different",
    "unrelated",
]


class MetricRelationship(BaseModel):
    metric_a_id: str
    metric_b_id: str

    relationship: RelationshipType