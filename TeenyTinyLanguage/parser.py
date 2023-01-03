import sys
from .lexer import *


class Parser:
    def __init__(self):
        pass

    def checkToken(self, kind):
        pass

    def checkPeek(self, kind):
        pass

    def match(self, kind):
        pass

    def nextToken(self):
        pass

    def abort(self, message):
        sys.exit("Error. " + message)
