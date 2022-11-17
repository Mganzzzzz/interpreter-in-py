from type import TokenType
from dataclasses import dataclass


@dataclass()
class Token:
    raw: str | int | float
    type: TokenType

    # 获取运算符的优先级
    def get_operator_priority(self) -> int:
        PriorityMap = {
            '+': 100,
            '-': 100,
            '*': 101,
            '/': 101,
        }
        ret = PriorityMap[self.raw]
        if ret > 0:
            return ret
