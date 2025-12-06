from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import ConfigDict, RootModel

from schemas.aircraft import AircraftSchema
from schemas.route import RouteSchema
from schemas.vertiport import VertiportSchema


class FlightStatusEnum(str, Enum):
    PENDING = "PENDING"
    ACTIVATED = "ACTIVATED"
    CANCELLED = "CANCELLED"
    TERMINATED = "TERMINATED"


class FlightInstanceSchema(Schema):
    id: UUID
    aircraft: AircraftSchema
    callsign: Optional[str] = None
    route: Optional[RouteSchema] = None
    flight_status: FlightStatusEnum
    departure_vertiport: Optional[VertiportSchema] = None
    arrival_vertiport: Optional[VertiportSchema] = None
    scheduled_departure_datetime: Optional[datetime] = None
    scheduled_arrival_datetime: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class FlightInstanceSchemaList(RootModel):
    root: list[FlightInstanceSchema]


class SubmitFlightInstance(Schema):
    aircraft: UUID
    callsign: Optional[str] = None
    route: Optional[UUID] = None
    flight_status: FlightStatusEnum
    departure_vertiport: Optional[UUID] = None
    arrival_vertiport: Optional[UUID] = None
    scheduled_departure_datetime: Optional[datetime] = None
    scheduled_arrival_datetime: Optional[datetime] = None


class UpdateFlightInstance(Schema):
    aircraft: Optional[UUID] = None
    callsign: Optional[str] = None
    route: Optional[UUID] = None
    flight_status: Optional[FlightStatusEnum] = None
    departure_vertiport: Optional[UUID] = None
    arrival_vertiport: Optional[UUID] = None
    scheduled_departure_datetime: Optional[datetime] = None
    scheduled_arrival_datetime: Optional[datetime] = None


class FlightInstanceFilterSchema(Schema):
    id: Optional[UUID] = None
    flight_status: Optional[FlightStatusEnum] = None
    departure_vertiport: Optional[UUID] = None
    arrival_vertiport: Optional[UUID] = None
    scheduled_departure_datetime: Optional[datetime] = None
    scheduled_arrival_datetime: Optional[datetime] = None
