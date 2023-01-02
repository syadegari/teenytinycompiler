import unittest
from .teenytiny_imports import *


class TestLexer(unittest.TestCase):
    def test_peek_and_nexChar(self):
        input = 'LET foobar = 123'
        lexer = Lexer(input)

        while lexer.peek() != '\0':
            self.assertEqual(lexer.curChar, input[lexer.curPos])
            lexer.nextChar()

    def test_getToken(self):
        input = '+- */'
        lexer = Lexer(input)

        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.PLUS)

        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.MINUS)

        token = lexer.getToken()

if __name__ == '__main__':
    unittest.main()