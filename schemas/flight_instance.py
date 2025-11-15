from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import ConfigDict

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
    scheduled_departure_datetime: datetime
    scheduled_arrival_datetime: datetime

    model_config = ConfigDict(from_attributes=True)
