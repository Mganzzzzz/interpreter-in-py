from dataclasses import dataclass
from typing import List
from enum import Enum

from token2 import Token
from type import TokenType
from utility import is_operator


@dataclass()
class Tokenizer:
    source: str
    i: int = 0

    @property
    def letter(self) -> str | None:
        try:
            return self.source[self.i]
        except:
            return None

    def parse(self) -> List[Token]:
        m: List[Token] = []
        n: Token | None = None
        while True:
            if not self.letter:
                break
            c = self.parse_word()
            if c:
                m.append(c)
                continue
            c = self.parse_space()
            if c:
                m.append(c)
                continue
            c = self.parse_number()
            if c:
                m.append(c)
                continue

            c = self.parse_operator()
            if c:
                m.append(c)
                continue

            c = self.parse_stringliteral()
            if c:
                m.append(c)
                continue
            c = self.parse_bracket()
            if c:
                m.append(c)
                continue

            c = self.parse_semicolon()
            if c:
                m.append(c)
                continue

            if c is None:
                break
        return m

    def parse_operator(self):
        if is_operator(self.letter):
            o = self.letter
            self.next_letter()
            return Token(o, TokenType.Operator)
        return None

    def next_letter(self):
        self.i += 1

    def parse_number(self):
        s = ''
        if self.letter.isnumeric():
            while self.letter.isnumeric():
                s += self.letter
                self.next_letter()
            n = int(s)
            return Token(n, TokenType.IntLiteral)
        return None

    def parse_space(self):
        if self.letter.isspace():
            self.next_letter()
            return Token(' ', TokenType.Space)
        return None

    def parse_word(self):
        s = ''
        c = self.letter
        if not c.isalpha():
            return None
        while c.isalpha() or c.isnumeric():
            s += c
            self.next_letter()
            c = self.letter
        ret = Token(s, TokenType.Identifier)
        return ret

    def parse_stringliteral(self):
        s = self.letter
        ret = ''
        if s == "'":
            self.next_letter()
            while self.letter != "'":
                ret += self.letter
                self.next_letter()
            self.next_letter()
            return Token(ret, TokenType.StringLiteral)
            # self.next_letter()
            # return Token(s, TokenType.SingleQuotation)
        elif s == '"':
            self.next_letter()
            while self.letter != '"':
                ret += self.letter
                self.next_letter()
            self.next_letter()
            return Token(ret, TokenType.StringLiteral)
        return None

    def parse_bracket(self):
        s = self.letter
        ret = None
        if s == "(":
            ret = Token(s, TokenType.LeftParenthesis)
        elif s == ')':
            ret = Token(s, TokenType.RightParenthesis)
        elif s == '[':
            ret = Token(s, TokenType.LeftBracket)
        elif s == ']':
            ret = Token(s, TokenType.RightBracket)
        elif s == '{':
            ret = Token(s, TokenType.LeftBraces)
        elif s == '}':
            ret = Token(s, TokenType.RightBrace)
        if ret:
            self.next_letter()
        return ret

    def parse_semicolon(self):
        if self.letter == ";":
            self.next_letter()
            return Token(';', TokenType.Semicolon)
        return None
