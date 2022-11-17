from dataclasses import dataclass, field
from typing import List

from ast2.object import Statement, Program, FunctionDecl, FunctionBody, Expression, FunctionParameter, FunctionCall
from token2 import Token
from type import TokenType


@dataclass()
class AstParser:
    """"""
    tokenList: List[Token]
    program: Program = field(default_factory=list)
    statement: List[Statement] = field(default_factory=list)
    index: int = 0

    @property
    def token(self) -> Token | None:
        try:
            return self.tokenList[self.index]
        except:
            return None

    def peek(self) -> Token | None:
        if self.index < len(self.tokenList):
            return self.tokenList[self.index + 1]

    def next(self) -> Token | None:
        if self.index < len(self.tokenList):
            self.index += 1
        return None

    def parse_func_decl(self) -> FunctionDecl | None:
        funcBody: FunctionBody
        token = self.token
        funcName: Token

        if not token:
            return None
        if token.type == TokenType.Identifier and token.raw == 'function':
            self.next()
            funcName = self.token
            self.next()
            self.next()
            funcBody = self.parse_func_body()
        else:
            return None
        return FunctionDecl(funcName, funcBody)

    def parse_func_body(self) -> FunctionBody | None:
        sm: List[Statement] = []
        while self.token.type != TokenType.RightBrace:
            functionCall = self.parse_func_call()
            if functionCall:
                sm.append(functionCall)
                continue
            self.next()
        self.next()
        return FunctionBody(sm)

    def parse_func_call(self) -> FunctionCall | None:
        if self.token.type != TokenType.Identifier:
            return None

        funcName = self.token
        params: FunctionParameter | None
        self.next()
        t = self.token
        if t.type == TokenType.LeftParenthesis:
            params = self.parse_func_params()
        else:
            raise Exception('function should call with ()')

        ref = self.find_function_decl()
        r = FunctionCall(funcName, ref, params)
        return r

    def parse_func_params(self):
        params = []
        # if(self.token.type != TokenType.LeftParenthesis:
        #     return None
        #
        # self.next()
        while self.token.type != TokenType.RightParenthesis:
            if self.token.type == TokenType.LeftParenthesis:
                self.next()
            elif self.token.type == TokenType.StringLiteral:
                params.append(self.token)
                self.next()
            elif self.token.type == TokenType.Comma:
                self.next()
            elif self.token.type == TokenType.SingleQuotation or self.token.type == TokenType.DoubleQuotation:
                s = self.parse_string_literal()
                params.append(s)
            else:
                raise Exception('function Parameter parse error')

        return FunctionParameter(params)

    def parse_string_literal(self):
        s = ''
        if self.token.type == TokenType.SingleQuotation:
            self.next()
            while self.token.type != TokenType.SingleQuotation:
                s += self.token.raw
                self.next()

            self.next()
            return Token(s, TokenType.Identifier)

        elif self.token.type == TokenType.DoubleQuotation:
            self.next()
            while self.token.type != TokenType.DoubleQuotation:
                s += self.token.raw
                self.next()

            self.next()
            return Token(s, TokenType.Identifier)

        return None

    def find_function_decl(self) -> FunctionDecl | None:
        ret = None
        for n in self.statement:
            if isinstance(n, FunctionDecl):
                ret = n
                break
        return ret

    def resolve_func_call_ref(self):
        ret = None
        for n in self.statement:
            if isinstance(n, FunctionCall):
                if n.funcRef is None:
                    n.funcRef = self.find_function_decl()
        return ret

    def parser_primary(self):
        t = self.token
        if t.type != TokenType.IntLiteral:
            return None

        ret = Expression(token=self.token, returnVal=None)
        st = Statement(self.token)
        # ret.statements.append(st)
        return ret

    def parse_binary(self, priority: int) -> Expression | None:
        """"""
        t = self.parser_primary()
        if not t:
            return None

        while True:
            token = self.token
            if token.type == TokenType.Space:
                break

            t = self.peek()
            if t.type == TokenType.Operator:
                p = t.get_operator_priority()
                print('debug p', p)
                if p > priority:
                    pass
            self.next()
        return None

    def parse_expression(self) -> Expression | None:
        t = self.token
        c = self.parse_binary(-100)
        return c

    def parse_program(self) -> Program | None:
        m: List[Statement] = []
        self.statement = m
        n: Statement | None = None
        while True:
            if self.token.type == TokenType.Space:
                self.next()
                continue

            n = self.parse_func_decl()
            if n:
                m.append(n)
                continue

            n = self.parse_expression()
            if n:
                m.append(n)
                continue

            n = self.parse_func_call()
            if n:
                m.append(n)
                continue
            if n is None:
                break

        prog = Program(m)
        self.resolve_func_call_ref()
        self.program = prog
        return prog
