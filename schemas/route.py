from typing import Optional
from uuid import UUID

from ninja import Schema

from schemas.vertiport import VertiportSchema


class RouteSchema(Schema):
    id: Optional[UUID] = None
    name: str
    departure_vertiport: Optional[VertiportSchema] = None
    arrival_vertiport: Optional[VertiportSchema] = None
