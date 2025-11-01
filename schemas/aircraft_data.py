from datetime import datetime
from typing import Optional
from uuid import UUID

from ninja import Schema

from schemas.aircraft import AircraftSchema


class AircraftDataSchema(Schema):
    id: Optional[UUID] = None
    aircraft: AircraftSchema
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    speed: Optional[float] = None
    energy_level: Optional[float] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
