from typing import Optional
from uuid import UUID

from ninja import Schema
from pydantic import ConfigDict

from schemas.vertiport import VertiportSchema


class RouteSchema(Schema):
    id: Optional[UUID] = None
    name: str
    departure_vertiport: Optional[VertiportSchema] = None
    arrival_vertiport: Optional[VertiportSchema] = None

    model_config = ConfigDict(from_attributes=True)
