from dataclasses import dataclass


@dataclass
class Discount:
    id: int
    name: str
    discount_percent: int
    desc: str | None
    created_at: str
    updated_at: str | None
    active: bool
