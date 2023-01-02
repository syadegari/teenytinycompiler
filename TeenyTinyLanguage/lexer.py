class Lexer:
    def __init__(self) -> None:
        pass

    # Process the next characther
    def nextChar(self):
        pass

    # Return the lookahead character
    def peek(self):
        pass

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


