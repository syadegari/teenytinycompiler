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
    def abort(self):
        pass

    # Skip the whitespace except newlines
    # Newlines are used to indicate the end of a statement.
    def skipWhitespace(self):
        pass

    # Skip comments
    def skipComment(self):
        pass

    # Return the next token
    def getToken(self):
        pass


