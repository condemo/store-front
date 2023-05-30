from typing import Protocol


class View(Protocol):
    def show(self) -> None:
        ...

    def remove(self) -> None:
        ...
