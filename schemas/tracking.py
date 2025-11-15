from datetime import datetime
from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import ConfigDict

from schemas.flight_instance import FlightInstanceSchema


class TrackingSchema(Schema):
    id: UUID
    flight_instance: FlightInstanceSchema
    name: Optional[str] = None
    latitude: float
    longitude: float
    altitude: float
    speed: float
    energy_level: float
    active: bool
    started_at: datetime
    finished_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
