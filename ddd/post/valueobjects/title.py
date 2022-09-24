import re
from dataclasses import dataclass

regex = r"^[a-zA-Z]{1,6}$"


@dataclass(eq=True, frozen=True)
class Title:
    value: str

    def __post_init__(self):
        if re.compile(regex).match(self.value) is None:
            raise ValueError("invalid error")
