from dataclasses import dataclass


@dataclass
class Stock:
    id: int
    qty: int
    updated_at: str | None
