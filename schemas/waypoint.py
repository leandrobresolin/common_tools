from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import ConfigDict

from schemas.route import RouteSchema
from schemas.vertiport import VertiportSchema


class WaypointSchema(Schema):
    id: UUID
    route: RouteSchema
    vertiport: Optional[VertiportSchema] = None
    name: Optional[str] = None
    latitude: float
    longitude: float
    altitude: Optional[float] = None
    sequence_order: int

    model_config = ConfigDict(from_attributes=True)
