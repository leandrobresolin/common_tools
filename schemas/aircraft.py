from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import RootModel

from schemas.aircraft_type import AircraftTypeSchema


class AircraftSchema(Schema):
    id: UUID
    tail_number: str
    model: AircraftTypeSchema
    year: Optional[int] = None


class AircraftSchemaList(RootModel):
    root: list[AircraftSchema]


class SubmitAircraftSchema(Schema):
    tail_number: str
    model: UUID
    year: Optional[int] = None


class UpdateAircraftSchema(Schema):
    tail_number: Optional[str] = None
    model: Optional[UUID] = None
    year: Optional[int] = None
