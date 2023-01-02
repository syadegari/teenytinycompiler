import unittest
from .teenytiny_imports import *


class TestLexer(unittest.TestCase):
    def test_peek_and_nexChar(self):
        input = 'LET foobar = 123'
        lexer = Lexer(input)

        while lexer.peek() != '\0':
            self.assertEqual(lexer.curChar, input[lexer.curPos])
            lexer.nextChar()


if __name__ == '__main__':
    unittest.main()