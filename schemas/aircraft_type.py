from enum import Enum
from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import RootModel


class EnergyTypeEnum(str, Enum):
    ELECTRIC = "ELECTRIC"
    FUEL = "FUEL"


class ModelTypeEnum(str, Enum):
    EVTOL = "EVTOL"
    DRONE = "DRONE"
    HELICOPTER = "HELICOPTER"


class AircraftTypeSchema(Schema):
    id: Optional[UUID] = None
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    energy_type: EnergyTypeEnum
    model_type: ModelTypeEnum


class AircraftTypeSchemaList(RootModel):
    root: list[AircraftTypeSchema]


class SubmitAircraftTypeSchema(Schema):
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    energy_type: EnergyTypeEnum
    model_type: ModelTypeEnum


class UpdateAircraftTypeSchema(Schema):
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    energy_type: Optional[EnergyTypeEnum] = None
    model_type: Optional[ModelTypeEnum] = None


class AircraftTypeFilterSchema(Schema):
    id: Optional[UUID] = None
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    energy_type: Optional[EnergyTypeEnum] = None
    model_type: Optional[ModelTypeEnum] = None
