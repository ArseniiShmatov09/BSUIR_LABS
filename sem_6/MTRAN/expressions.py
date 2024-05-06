class Expr:
    pass

class LiteralExpr(Expr):
    def __init__(self, token):
        self.token = token

class SymbolExpr(Expr):
    def __init__(self, token):
        self.token = token

class DefineExpr(Expr):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

class CallExpr(Expr):
    def __init__(self, called, args):
        self.called = called
        self.args = args


class SetExpr(Expr):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class LambdaExpr(Expr):
    def __init__(self, args, body, isSpread = False):
        self.args = args
        self.body = body
        self.isSpread = isSpread

class FuncExpr(LambdaExpr):
    pass


class IfExpr(Expr):
    def __init__(self, condition, trueExpr, falseExpr):
        self.condition = condition
        self.trueExpr = trueExpr
        self.falseExpr = falseExpr

class QuoteExpr:
    def __init__(self, value):
        self.value = value

class ListExpr(Expr):
    def __init__(self, items):
        self.items = items

class BeginExpr(Expr):
    def __init__(self, expression):
        self.expression = expression

class ImportExpr(Expr):
    def __init__(self, value):
        self.value = value

class ReturnExpr(Expr):
    def __init__(self, value):
        self.value = value


NULL_VALUE = []
