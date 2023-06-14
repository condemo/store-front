from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Providers:
    id: int
    name: str
    email: Optional[str] = "Vacío"
    contact_name: Optional[str] = "Vacío"
    phone: Optional[str] = "Vacio"
    web_url: Optional[str] = "Vacío"
    created_at: datetime
    updated_at: Optional[datetime] = None
