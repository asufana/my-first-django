from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Id:
    value: int

    def __post_init__(self):
        if self.value <= 0:
            raise ValueError("invalid error")
