from expressions import *
from environment import Environment
import math
from errors2 import SemanticError 
import sys
import re


class Interpreter:
    def __init__(self, expressions):
        self.expressions = expressions
        self.env = Environment()

        self.env.define("+", self.add)
        self.env.define("-", lambda a, b: self._check_number_and_compute(a, b, lambda x, y: x - y))
        self.env.define("/", lambda a, b: self._check_number_and_compute(a, b, lambda x, y: x / y))
        self.env.define("*", lambda a, b: self._check_number_and_compute(a, b, lambda x, y: x * y))
        self.env.define("=", lambda a, b: self._check_number_and_compute(a, b, lambda x, y: x == y))
        self.env.define(">", lambda a, b: self._check_number_and_compute(a, b, lambda x, y: x > y))
        self.env.define("<", lambda a, b: self._check_number_and_compute(a, b, lambda x, y: x < y))
        self.env.define(">=", lambda a, b: self._check_number_and_compute(a, b, lambda x, y: x >= y))
        self.env.define("<=", lambda a, b: self._check_number_and_compute(a, b, lambda x, y: x <= y))
        self.env.define("min", lambda a, b: self._check_number_and_compute(a, b, math.min))
        self.env.define("max", lambda a, b: self._check_number_and_compute(a, b, math.max))
        self.env.define("abs", lambda a: self._check_number_and_compute(a, math.abs))
        self.env.define("sqrt", lambda a: self._check_number_and_compute(a, math.sqrt))
        self.env.define("expt", lambda a: self._check_number_and_compute(a, math.exp))
        self.env.define("sin", lambda a: self._check_number_and_compute(a, math.sin))
        self.env.define("cos", lambda a: self._check_number_and_compute(a, math.cos))
        self.env.define("log", lambda a: self._check_number_and_compute(a, math.log))
        self.env.define("not", lambda a: not a if isinstance(a, bool) else False)
        self.env.define("display", lambda a: sys.stdout.write(self.to_lisp_types(a)+'\n'))
        self.env.define("null?", lambda a: a is None)
        self.env.define("number?", lambda a: isinstance(a, (int, float)))
        self.env.define("boolean?", lambda a: isinstance(a, bool))
        self.env.define("string?", lambda a: isinstance(a, str))
        self.env.define("list?", lambda a: isinstance(a, list))
        self.env.define("string-append", lambda str1, str2: str1 + str2)
        self.env.define("quote", lambda arg: arg)
        self.env.define("car", lambda arg: arg[0])
        self.env.define("cdr", lambda arg: arg[1:])
   
    def interpret(self, expressions=None):
        result = None
        expressions = expressions or self.expressions
        for expr in expressions:
            result = self.interpret_expr(expr, self.env)
        return self.to_lisp_types(result)
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise SemanticError(f"Wrong type for addition: {type(a)}, {type(b)}")
        return a + b

    def subtract(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise SemanticError(f"Wrong type for subtraction: {type(a)}, {type(b)}")
        return a - b

    def to_lisp_types(self, arg):
        if isinstance(arg, bool):
            return "#t" if arg else "#f"
        if isinstance(arg, str):
            arg_without_quotes = arg.strip('"') 
            return re.sub(r'\\(.)', lambda match: '\n' if match.group(1) == 'n' else match.group(0), arg_without_quotes)
        if isinstance(arg, list):
            return "(" + " ".join(map(self.to_lisp_types, arg)) + ")"
        return str(arg)
        
    def interpret_expr(self, expr, env):
        if isinstance(expr, CallExpr):
            called = self.interpret_expr(expr.called, env)
            args = []
            for arg in expr.args:
                args.append(self.interpret_expr(arg, env))
                        
            if isinstance(called, Procedure):
                if len(called.args) != len(args): #!!!!!
                    raise SemanticError(f"Wrong number of arguments in {expr.called.token.name} "f"(it takes {len(called.args)} arguments, but {len(args)} are received)")
                return called.call(self, args)

            
            cal = called(*args)
            return cal
        elif isinstance(expr, DefineExpr):
            return env.define(expr.variable.name, self.interpret_expr(expr.value, env))

        elif isinstance(expr, LambdaExpr):
             return Procedure(expr.args, expr.body, env)
       
        elif isinstance(expr, LiteralExpr):
            return expr.token.name

        elif isinstance(expr, SymbolExpr):
            return env.get(expr.token.name)
       
        elif isinstance(expr, QuoteExpr):
            return self.interpret_expr(expr.value, env)

        elif isinstance(expr, ListExpr):
            return [self.interpret_expr(value, env) for value in expr.items]
       
        elif isinstance(expr, IfExpr):
            condition_value = self.interpret_expr(expr.condition, env)
            if condition_value:
                return self.interpret_expr(expr.trueExpr, env)
            else:
                return self.interpret_expr(expr.falseExpr, env)


    def _check_number_and_compute(self, a, b, operation):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise SemanticError(f"Wrong type for function: {type(a)}, {type(b)}")
        return operation(a, b)

class Procedure:
    def __init__(self, args, body, env):
        self.args = args
        self.body = body
        self.env = env

    def call(self, interpreter, args):
        env = Environment(self.env, self.args, args)
        result = None
        for expr in self.body:
            result = interpreter.interpret_expr(expr, env)
        return result
