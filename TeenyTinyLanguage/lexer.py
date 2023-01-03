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
        if self.curChar == '#':
            while self.curChar != '\n':
                self.nextChar()

    # Return the next token
    def getToken(self) -> Token:
        self.skipWhitespace()
        self.skipComment()
        # + PLUS
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        # - MINUS
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        # * ASTERISK
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        # / SLASH
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        # \n NEWLINE
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)
        # = EQ and == EQEQ
        elif self.curChar == '=':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.EQEQ)
            else:
                token = Token(self.curChar, TokenType.EQ)
        # < LT and <= LTEQ
        elif self.curChar == '<':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.LTEQ)
            else:
                token = Token(self.curChar, TokenType.LT)
        # > GT and >= GTEQ
        elif self.curChar == '>':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.GTEQ)
            else:
                token = Token(self.curChar, TokenType.GT)
        # != NOTEQ
        elif self.curChar == '!':
            if self.peek() == '=':
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)
            else:
                self.abort("Expected !=, got !" + self.curChar)
        # STRING
        elif self.curChar == '\"':
            self.nextChar()
            startPos = self.curPos
            while self.curChar != '\"':
                if self.curChar in {'\r', '\n', '\\', '\t', '%'}:
                    self.abort('Illegal character in string: ' + self.curChar)
                self.nextChar()
            token = Token(self.source[startPos : self.curPos], TokenType.STRING)
        # NUMBER
        elif self.curChar.isdigit():
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.':
                self.nextChar()
                if not self.peek().isdigit():
                    self.abort('Must follow by at least one digit after decimal point')
                while self.peek().isdigit():
                    self.nextChar()
            token = Token(self.source[startPos : self.curPos + 1], TokenType.NUMBER)
        # IDENT and keyword
        elif self.curChar.isalpha():
            startPos = self.curPos
            while self.peek().isalnum():
                self.nextChar()
            tokText = self.source[startPos : self.curPos + 1]
            keyword = TokenType.checkIfKeyword(tokText)
            if keyword == None:
                token = Token(tokText, TokenType.IDENT)
            else:
                token = Token(tokText, keyword)
        # \0 EOF
        elif self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)
        else:
            # unknown token
            self.abort("Unknown token: " + self.curChar)

        self.nextChar()
        return token

    def __repr__(self) -> str:
        return self.curChar


