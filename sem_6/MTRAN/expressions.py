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

class LambdaExpr(Expr):
    def __init__(self, args, body):
        self.args = args
        self.body = body

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

NULL_VALUE = []
