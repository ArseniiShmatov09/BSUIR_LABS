from Token import Token
from Token_type import Token_type
from expressions import CallExpr, DefineExpr, IfExpr, LambdaExpr, LiteralExpr, NULL_VALUE, SymbolExpr, ListExpr, QuoteExpr

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        expressions = []
        while not self.isEnd():
            expressions.append(self.expression())
        return expressions

    def expression(self):
        if self.match('openedBracket'):
            if self.match('closedBracket'):
                raise SyntaxError(f"Ошибка синтаксиса () [{self.previous().pos}]")

            token = self.peek()
            if token.name == 'define':
                return self.define()
            if token.name == 'lambda':
                return self.lambda_()
            if token.name == 'if':
                return self.if_()
            if token.name == 'quote':
                return self.quote()
            return self.call()
        return self.atom()

    def call(self):
        called = self.expression()

        if called.token.type.name != 'symbol':
            raise SyntaxError(f"Неизвестный токен [{called.token.pos} : {called.token.name}")

        args = []
        while not self.match('closedBracket'):
            args.append(self.expression())

        return CallExpr(called, args)

    def quote(self):
        self.advance()
        value = self.quoteValue()

        if self.peek().type.name == 'closedBracket':
            self.advance()
        else:
            raise SyntaxError()

        return QuoteExpr(value)

    def quoteValue(self):
        if self.match('openedBracket'):
            args = []
            while not self.match('closedBracket'):
                params = self.expression()
                args.append(params)
            return ListExpr(args)
        else:
            return self.expression()

    def define(self):
        self.advance()
        variable = self.advance()

        if variable.type.name != 'symbol':
            raise SyntaxError(f"Неверное имя переменной [{variable.pos} : ] {variable.name}")
        expr = self.expression()

        if not self.match('closedBracket'):
            raise SyntaxError('Не закрыта скобка')

        return DefineExpr(variable, expr)

    def lambda_(self):
        self.advance()
        args = []

        if self.match('symbol'):
            args.append(self.previous())
        else:
            if not self.match('openedBracket'):
                raise SyntaxError()

            while not self.match('closedBracket'):
                if not self.match('symbol'):
                    raise SyntaxError(f"Неопределенный аргумент [{self.peek().pos}]: {self.peek().name}")

                if any(arg.name == self.previous().name for arg in args):
                    raise SyntaxError(f"Дублирование аргумента функции [{self.previous().pos}]: {self.previous().name}")

                args.append(self.previous())

        body = []
        while not self.match('closedBracket'):
            body.append(self.expression())

        return LambdaExpr(args, body)

    def if_(self):
        self.advance()
        condition = self.expression()
        trueExpr = self.expression()

        falseExpr = None
        if self.peek().type.name == 'openedBracket':
            falseExpr = self.expression()

        if not self.match('closedBracket'):
            raise SyntaxError('Не закрыта скобка')

        return IfExpr(condition, trueExpr, falseExpr)

    def atom(self):
        if self.match('symbol'):
            return SymbolExpr(self.previous())
        elif self.match('boolean') or self.match('string') or self.match('number'):
            return LiteralExpr(self.previous())
        else:
            raise SyntaxError('Не закрыта скобка')

    def previous(self):
        return self.tokens[self.current - 1]

    def advance(self):
        self.current += 1
        return self.tokens[self.current - 1]

    def match(self, tokenType):
        
        if self.peek().type.name == tokenType:
            self.current += 1
            return True
        return False

    def peek(self):
        return self.tokens[self.current]

    def isEnd(self):
        return self.peek().type == 'eof'