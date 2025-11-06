from datetime import datetime
from typing import Optional
from uuid import UUID

from ninja import Schema


class VertiportSchema(Schema):
    id: UUID
    vertiport_code: str
    vertiport_name: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    created_at: datetime
