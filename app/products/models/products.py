from dataclasses import dataclass
from uuid import UUID

from .stock import Stock
from .category import Category
from .discount import Discount
from .brand import Brand


@dataclass
class ProductMin:
    id: int
    name: str
    category: str
    price: float


@dataclass
class ProductFull:
    id: int
    name: str
    price: float
    provider_price: float
    brand: Brand
    category: Category
    discount: Discount
    stock: Stock
    uuid: UUID
    created_at: str
