from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import ConfigDict, RootModel


class RouteSchema(Schema):
    id: Optional[UUID] = None
    name: str

    model_config = ConfigDict(from_attributes=True)


class RouteSchemaList(RootModel):
    root: list[RouteSchema]


class SubmitRouteSchema(Schema):
    name: str


class UpdateRouteSchema(Schema):
    name: str


class RouteFilterSchema(Schema):
    id: Optional[UUID] = None
    name: Optional[str] = None
