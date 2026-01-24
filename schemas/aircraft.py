from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import ConfigDict, RootModel

from schemas.aircraft_type import AircraftTypeSchema


class AircraftSchema(Schema):
    id: UUID
    tail_number: str
    aircraft_type: AircraftTypeSchema
    year: Optional[int] = None
    energy_fuel: Optional[float] = None

    model_config = ConfigDict(from_attributes=True)


class AircraftSchemaList(RootModel):
    root: list[AircraftSchema]


class SubmitAircraftSchema(Schema):
    tail_number: str
    aircraft_type: UUID
    year: Optional[int] = None
    energy_fuel: Optional[float] = None


class UpdateAircraftSchema(Schema):
    tail_number: Optional[str] = None
    aircraft_type: Optional[UUID] = None
    year: Optional[int] = None
    energy_fuel: Optional[float] = None


class AircraftFilterSchema(Schema):
    id: Optional[UUID] = None
    tail_number: Optional[str] = None
    aircraft_type: Optional[UUID] = None
    year: Optional[int] = None
