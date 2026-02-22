from datetime import datetime
from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import ConfigDict, RootModel

from schemas.flight_instance import FlightInstanceSchema


class AircraftDataSchema(Schema):
    id: Optional[UUID] = None
    flight_instance: FlightInstanceSchema
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    speed: Optional[float] = None
    energy_level: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class AircraftDataSchemaList(RootModel):
    root: list[AircraftDataSchema]


class AircraftDataFilterSchema(Schema):
    id: Optional[UUID] = None
    flight_instance: Optional[UUID] = None
    aircraft: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    created_from: Optional[datetime] = None
    created_to: Optional[datetime] = None
