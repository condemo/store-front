from typing import TypedDict
from datetime import datetime


class EventCard(TypedDict):
    event_type: str
    text: str
    date: datetime
