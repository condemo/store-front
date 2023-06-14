from dataclasses import dataclass
from .providers import Providers
from products.models import ProductListed
from typing import Optional
from datetime import date, datetime


@dataclass
class Orders:
    id: int
    paid: bool
    received: bool
    provider: Providers
    products_listed: list[ProductListed]
    qty: int
    approx_delivery_date: Optional[date] = "Sin fecha"
    created_at: datetime
    update_at: Optional[datetime] = "No actualizado"
