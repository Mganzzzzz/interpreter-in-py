from dataclasses import dataclass, field
from typing import List, Any

from token2 import Token


@dataclass()
class Statement:
    """statment 并没有什么value 返回, 只是一个动作而已"""
    token: List[Token]


@dataclass()
class Expression(Statement):
    """Expression 有返回值"""
    returnVal: Any = None


@dataclass()
class FunctionBody:
    statement: List[Statement] = field(default_factory=list)


@dataclass()
class FunctionParameter:
    parameter: List[Token] = field(default_factory=list)


@dataclass()
class FunctionDecl:
    """函数就是一大堆statement的集合, 因为它是做一件事的具体步骤, 都是动作"""
    funcName: Token
    funcBody: FunctionBody
    token: List[Token] = field(default_factory=list)


@dataclass()
class FunctionCall:
    funcName: Token
    funcRef: FunctionDecl
    functionParameter: FunctionParameter


@dataclass()
class Program:
    statement: List[Statement] = field(default_factory=list)
