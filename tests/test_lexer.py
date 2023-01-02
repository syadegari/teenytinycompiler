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
        input = '+- */ >>= = !='
        lexer = Lexer(input)

        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.PLUS)

        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.MINUS)

        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.ASTERISK)

        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.SLASH)

        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.GT)

        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.GTEQ)

        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.EQ)

        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.NOTEQ)

        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.NEWLINE)

    def test_comment(self):
        input = '>= +  # The rest is a comment'
        lexer = Lexer(input)
        self.assertEqual(lexer.getToken().kind, TokenType.GTEQ)
        self.assertEqual(lexer.getToken().kind, TokenType.PLUS)
        # comment begins here, should ignore until newline is reached
        self.assertEqual(lexer.getToken().kind, TokenType.NEWLINE)

        input ='# This line is a comment'
        lexer = Lexer(input)
        self.assertEqual(lexer.getToken().kind, TokenType.NEWLINE)

        input = '   # whitespace before comment begins'
        lexer = Lexer(input)
        self.assertEqual(lexer.getToken().kind, TokenType.NEWLINE)

    def test_string(self):
        input = '+- \"Hello World\" # Some comments here!\n */'
        lexer = Lexer(input)
        self.assertEqual(lexer.getToken().kind, TokenType.PLUS)
        self.assertEqual(lexer.getToken().kind, TokenType.MINUS)
        self.assertEqual(lexer.getToken().kind, TokenType.STRING)
        self.assertEqual(lexer.getToken().kind, TokenType.NEWLINE)
        self.assertEqual(lexer.getToken().kind, TokenType.ASTERISK)
        self.assertEqual(lexer.getToken().kind, TokenType.SLASH)
        self.assertEqual(lexer.getToken().kind, TokenType.NEWLINE)

    def test_number(self):
        input = "+-123 9.8654*/"
        lexer = Lexer(input)

        self.assertEqual(lexer.getToken().kind, TokenType.PLUS)
        self.assertEqual(lexer.getToken().kind, TokenType.MINUS)
        #
        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.NUMBER)
        self.assertEqual(token.text, '123')
        #
        token = lexer.getToken()
        self.assertEqual(token.kind, TokenType.NUMBER)
        self.assertEqual(token.text, '9.8654')
        #
        self.assertEqual(lexer.getToken().kind, TokenType.ASTERISK)
        self.assertEqual(lexer.getToken().kind, TokenType.SLASH)
        self.assertEqual(lexer.getToken().kind, TokenType.NEWLINE)

if __name__ == '__main__':
    unittest.main()
