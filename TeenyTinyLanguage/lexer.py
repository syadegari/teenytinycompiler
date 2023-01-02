import sys
from .lang_token import Token, TokenType

class Lexer:
    def __init__(self, input) -> None:
        self.source = input + '\n'
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    # Process the next characther
    def nextChar(self) -> None:
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]

    # Return the lookahead character
    def peek(self) -> str:
        peekPos = self.curPos + 1
        if peekPos >= len(self.source):
            return '\0'
        else:
            return self.source[peekPos]

    # For an invalid token, print an error message and quit
    def abort(self, message) -> None:
        sys.exit("Lexing error. " + message)

    # Skip the whitespace except newlines
    # Newlines are used to indicate the end of a statement.
    def skipWhitespace(self) -> None:
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

    # Skip comments
    def skipComment(self):
        pass

    # Return the next token
    def getToken(self) -> Token:
        self.skipWhitespace()

        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)
        elif self.curChar == '=':
            token = Token(self.curChar, TokenType.EQ)
        elif self.curChar == '<':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.LTEQ)
            else:
                token = Token(self.curChar, TokenType.LT)
        elif self.curChar == '>':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.GTEQ)
            else:
                token = Token(self.curChar, TokenType.GT)
        elif self.curChar == '!':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)
            else:
                self.abort("Expected !=, got !" + self.curChar)
        elif self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)
        else:
            # unknown token
            self.abort("Unknown token: " + self.curChar)

        self.nextChar()
        return token

    def __repr__(self) -> str:
        return self.curChar


