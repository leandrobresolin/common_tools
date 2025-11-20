from datetime import datetime
from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import ConfigDict, RootModel


class VertiportSchema(Schema):
    id: UUID
    vertiport_code: str
    vertiport_name: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class VertiportSchemaList(RootModel):
    root: list[VertiportSchema]


class SubmitVertiportSchema(Schema):
    vertiport_code: str
    vertiport_name: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None


class UpdateVertiportSchema(Schema):
    vertiport_code: Optional[str] = None
    vertiport_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None


class VertiportFilterSchema(Schema):
    id: Optional[UUID] = None
    vertiport_code: Optional[str] = None
    vertiport_name: Optional[str] = None
