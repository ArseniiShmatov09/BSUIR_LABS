from errors2 import SemanticError

class Environment:

    def __init__(self, closest_env=None, keys=None, values=None):
        self.declarations = {}

        if keys is not None and values is not None:
            if not self._is_arrays(keys, values):
                raise ValueError("Keys and values must both be arrays or neither.")
            
            if self._is_arrays(keys, values):
                if len(keys) != len(values):
                    raise ValueError("Keys and values must be the same length.")
                for i in range(len(keys)):
                    self.declarations[keys[i].name] = values[i]
            else:
                self.declarations[keys.name] = values

        self.closest_env = closest_env


    @staticmethod
    def _is_arrays(keys, values):
        return isinstance(keys, list) == isinstance(values, list)

    def define(self, key, value):
        self.declarations[key] = value

    def set(self, key, value):
        if key in self.declarations:
            self.declarations[key] = value
            return
        if self.closest_env:
            self.closest_env.set(key, value)
            return
        raise ValueError("Variable not defined in the current scope.")

    def get(self, key):
        if key in self.declarations:
            return self.declarations[key]
        if self.closest_env:
            return self.closest_env.get(key)
        raise SemanticError(f"Unbound variable '{key}'")
