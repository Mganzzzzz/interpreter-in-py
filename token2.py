from type import TokenType
from dataclasses import dataclass

@dataclass()
class Token:
    raw: str | int | float
    type: TokenType
