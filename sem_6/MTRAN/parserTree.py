from Token import Token
from Token_type import Token_type
from expressions import *

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
            if token.name == 'set!':
                return self.set()
            if token.name == 'begin':
                return self.begin()
            if token.name == 'import':
                return self.import_()
            if token.name == 'return':
                return self.return_()
            
            
            return self.call()
        return self.atom()

    def return_(self):
        self.advance()
        value = self.expression()
        self.advance()
        return ReturnExpr(value)

    def import_(self):
        self.advance()
        value = self.expression()
        self.advance()
        return ImportExpr(value)

    def begin(self):
        self.advance()
        expr = []
        while not self.match('closedBracket'):
            expr.append(self.expression())
        return BeginExpr(expr)

    def call(self):
        called = self.expression()

        if called.token.type.name != 'symbol':
            raise SyntaxError(f"Неизвестный токен [{called.token.pos} : {called.token.name}]")

        args = []
        while not self.match('closedBracket'):
            args.append(self.expression())

        return CallExpr(called, args)

    def set(self):
        self.advance()
        name = None
        if str(self.peek().type.name) == 'symbol':
            name = self.advance()
        else:
            raise SyntaxError("Unexpected token")
        
        value = self.expression()

        if self.peek().type.name == 'closedBracket':
            self.advance()
        else:
            raise SyntaxError("Unexpected token")
        
        return SetExpr(name, value)

    def quote(self):
        self.advance()
        value = self.quote_value()

        if self.peek().type.name == 'closedBracket':
            self.advance()
        else:
            raise SyntaxError()

        return QuoteExpr(value)

    def quote_value(self):
        if self.match('openedBracket'):
            args = []
            while self.peek().type.name != 'closedBracket':
                if self.peek().type.name == 'openedBracket':
                    args.append(self.quote_value())
                    continue
                params = self.expression()
                args.append(params)
            self.advance()
            quoted = ListExpr(args)
        else:
            quoted = self.expression()
        return quoted

    def define(self):
        self.advance()
        variable = self.advance()
        expr = None

        if variable.type.name == 'openedBracket':
            variable = self.advance()
            expr = self.func()
            return DefineExpr(variable, expr)

        if variable.type.name != 'symbol':
            raise SyntaxError(f"Unexpected name [{variable.pos}] {variable.name}")

        try:
            expr = self.expression()
        except:
            expr = None

        if not self.match('closedBracket'):
            raise SyntaxError("Unexpected EOF")
        return DefineExpr(variable, expr)

    def get_func_arguments(self):
        args = []
        while not self.match('closedBracket'):
            if not self.match('symbol'):
                raise SyntaxError(f"Invalid list of argument [{self.peek().line}:{self.peek().position}]: {self.peek().lexeme}")
            if any(arg.name == self.previous().name for arg in args):
                raise SyntaxError(f"Duplicate identifier in argument list [{self.previous().pos}]: {self.previous().name}")
            args.append(self.previous())
        return args

    def func(self):
        args = self.get_func_arguments()
        body = []

        while not self.match('closedBracket'):
            body.append(self.expression())

        return FuncExpr(args, body)

    def lambda_(self):
        self.advance()
        is_spread = False

        args = []
        if self.match('symbol'):
            args.append(self.previous())
            is_spread = True
        else:
            if not self.match('openedBracket'):
                raise SyntaxError()
            args.extend(self.get_func_arguments())
        
        body = []
        while not self.match('closedBracket'):
            body.append(self.expression())

        return LambdaExpr(args, body, is_spread)

    def if_(self):
        self.advance()
        condition = self.expression()
        true_expr = self.expression()
        false_expr = None
        if not self.match('closedBracket') or self.match('openedBracket'):
            false_expr = self.expression()
        if false_expr:
            self.advance()
        return IfExpr(condition, true_expr, false_expr)

    def atom(self):
        if self.match('symbol'):
            return SymbolExpr(self.previous())
        elif self.match('quote'):
            return self.quote_value()
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