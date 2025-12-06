from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import ConfigDict, RootModel, model_validator

from schemas.route import RouteSchema
from schemas.vertiport import VertiportSchema


class WaypointSchema(Schema):
    id: UUID
    route: RouteSchema
    vertiport: Optional[VertiportSchema] = None
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    sequence_order: int

    model_config = ConfigDict(from_attributes=True)


class WaypointSchemaList(RootModel):
    root: list[WaypointSchema]


class SubmitWaypointSchema(Schema):
    route: UUID
    vertiport: Optional[UUID] = None
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    sequence_order: int

    @model_validator(mode="after")
    def check_location_when_no_vertiport(self):
        # If no vertiport is provided, latitude AND longitude are required
        if self.vertiport is None:
            if self.latitude is None or self.longitude is None:
                raise ValueError(
                    "Latitude and longitude are required when vertiport is not provided."
                )
        return self


class UpdateWaypointSchema(Schema):
    route: Optional[UUID] = None
    vertiport: Optional[UUID] = None
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    sequence_order: Optional[float] = None


class WaipointFilterSchema(Schema):
    id: Optional[UUID] = None
    route: Optional[UUID] = None
    vertiport: Optional[UUID] = None
    name: Optional[str] = None
