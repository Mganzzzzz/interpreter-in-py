from enum import Enum


class TokenType(Enum):
    Identifier = 'Identifier',
    KeyWord = 'KeyWord',  #
    LeftBracket = 'LeftBracket',  # [
    RightBracket = 'RightBracket',  # ]
    LeftParenthesis = 'LeftParenthesis',  # (
    RightParenthesis = 'RightParenthesis',  # )
    LeftBraces = 'LeftBraces',  # {
    RightBrace = 'RightBrace',  # }
    SingleQuotation = 'SingleQuotation',  # '
    DoubleQuotation = 'DoubleQuotation',  # "
    DoubleSlashes = 'DoubleSlashes',  # #
    SingleSlash = 'SingleSlash',  # /
    Semicolon = 'Semicolon',  # ;
    Comma = 'Comma',  # ,
    Space = 'Space',  # ,
    StringLiteral = 'StringLiteral',  # string
    IntLiteral = 'IntLiteral',  # number
    FloatLiteral = 'FloatLiteral',  # number
    Operator = 'Operator',  # number
