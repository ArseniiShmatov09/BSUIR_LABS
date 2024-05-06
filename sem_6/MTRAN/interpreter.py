from expressions import *
from environment import *
import math
from errors2 import * 
import sys
import re
import os
from Token_type import *
from const import *
from Token import *
from utils import *
from parserTree import Parser

class Interpreter:
    def __init__(self, expressions):
        self.expressions = expressions
        self.env = Environment()
        self.imported_files = []

        self.env.define("set!", lambda key, value: self.env.set(key, value))
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
        self.env.define("list", lambda *args: self.create_list(args))
        self.env.define('vector-ref', lambda list, index: vector_ref(list,index))
        self.env.define('vector-set!', lambda list, index, value: vector_set(list,index, value))
        self.env.define('make-list', lambda size, value: make_list(size, value))
   

        def vector_ref(list, index):
            if isinstance(index, int) and index >= 0 and index < len(list):
                return list[index]
            else:
                raise SemanticError(f"In procedure 'vector-ref' Wrong type '{index}'")

        def vector_set(list, index, value):
            if isinstance(index, int) and index >= 0 and index < len(list):
                list[index] = value
                return list
            else:
                raise SemanticError(f"In procedure 'vector-set!' Wrong type '{index}'")

        def make_list(size, value):
            if not isinstance(value, list):
                return [value] * size
            else:
                return [value[:] for _ in range(size)]

    def create_list(*args):
        return list(args)

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
        if arg is None:
            return 'unspecified'
        if callable(arg):
            return f"procedure {self.env.get_key_by_value(arg)}"
        if isinstance(arg, Procedure):
            return f"procedure {self.env.get_key_by_value(arg)}"
        
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
        if isinstance(expr, DefineExpr):
            return env.define(expr.variable.name, self.interpret_expr(expr.value, env))

        if isinstance(expr, LambdaExpr):
             return Procedure(expr.args, expr.body, expr.isSpread, env)
       
        if isinstance(expr, LiteralExpr):
            return expr.token.name

        if isinstance(expr, SymbolExpr):
            return env.get(expr.token.name)
       
        if isinstance(expr, SetExpr):
            return env.set(expr.name.name, self.interpret_expr(expr.value, env))
       
        if isinstance(expr, QuoteExpr):
            return self.interpret_expr(expr.value, env)

        if isinstance(expr, ListExpr):
            return [self.interpret_expr(value, env) for value in expr.items]
       
        if isinstance(expr, IfExpr):
            condition_value = self.interpret_expr(expr.condition, env)
            if condition_value:
                return self.interpret_expr(expr.trueExpr, env)
            else:
                return self.interpret_expr(expr.falseExpr, env)
       
        if isinstance(expr, BeginExpr):
            return self.interpret(expr.expression, env)

        if isinstance(expr, ImportExpr):
            file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), expr.value.token.name)

            if os.path.splitext(file_path)[1] == '.scm':
                return self.import_if_exist_and_not_imported(file_path, env)

            if os.path.splitext(file_path)[1] == '':
                file_path_with_ext = file_path + '.scm'
                return self.import_if_exist_and_not_imported(file_path_with_ext, env)

            raise RuntimeError(f"Cannot import file: {file_path}")

        if isinstance(expr, ReturnExpr):
            return self.interpret_expr(expr.value, env)

    def _check_number_and_compute(self, a, b, operation):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise SemanticError(f"Wrong type for function: {type(a)}, {type(b)}")
        return operation(a, b)

    def is_imported(self, file_path):
        return os.path.abspath(file_path) in self.imported_files

    def import_if_exist_and_not_imported(self, file_path, env):
        if os.path.exists(file_path):
            return self.import_if_not_imported(file_path, env)
        else:
            raise RuntimeError(f"Cannot import file: {file_path}")

    def import_if_not_imported(self, file_path, env):
        if self.is_imported(file_path):
            return
        self.imported_files.append(os.path.abspath(file_path))
        return self.import_file(file_path, env)

    def import_file(self, file_path, env):
        with open(file_path, 'r') as file:
            file_content = file.read()

        result = get_token_table(file_content) 
        tokens = result[0]
        parser = Parser(tokens)
        expressions = parser.parse()         
        return self.interpret(expressions, env)

class Procedure:
    def __init__(self, args, body, isSpread, env):
        self.args = args
        self.body = body
        self.isSpread = isSpread
        self.env = env

    def call(self, interpreter, args):
        if self.isSpread:
            args = [args]
        env = Environment(self.env, self.args, args)
        result = None
        for expr in self.body:
            result = interpreter.interpret_expr(expr, env)
            if isinstance(expr, ReturnExpr):
                break
        return result
