from datetime import datetime
from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import ConfigDict, RootModel

from schemas.flight_instance import FlightInstanceSchema


class TrackingSchema(Schema):
    id: UUID
    flight_instance: FlightInstanceSchema
    latitude: float
    longitude: float
    altitude: float
    speed: float
    energy_level: float
    active: bool
    started_at: datetime
    finished_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class TrackingSchemaList(RootModel):
    root: list[TrackingSchema]


class SubmitTrackingSchema(Schema):
    flight_instance: UUID
    latitude: float
    longitude: float
    altitude: float
    speed: float
    energy_level: float
    active: bool
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class TrackingFilterSchema(Schema):
    id: Optional[UUID] = None
    flight_instance: Optional[UUID] = None
    active: Optional[bool] = None
