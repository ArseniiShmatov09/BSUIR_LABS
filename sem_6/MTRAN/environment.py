from errors2 import SemanticError

class Environment:
    """
    :param closest_env: Environment object
    :param keys: Token object or list of Token objects
    :param values: any object or list of any objects
    """
    def __init__(self, closest_env=None, keys=None, values=None):
        self.declarations = {}
        if keys is not None and values is not None:
            if not self.is_arrays(keys, values):
                raise ValueError("Keys and values must have the same type")

            if isinstance(keys, list):
                if len(keys) != len(values):
                    raise ValueError("Length of keys and values must be the same")
                for i in range(len(keys)):
                    self.declarations[keys[i].name] = values[i]
            else:
                self.declarations[keys.name] = values
        self.closest_env = closest_env

    def get_key_by_value(self, value):
        for key, val in self.declarations.items():
            if val == value:
                return key
        return None

    @staticmethod
    def is_arrays(keys, values):
        return not (isinstance(keys, list) and not isinstance(values, list) or
                    not isinstance(keys, list) and isinstance(values, list))

    def define(self, key, value):
        self.declarations[key] = value

    def set(self, key, value):
        if key in self.declarations:
            self.declarations[key] = value
        elif self.closest_env:
            self.closest_env.set(key, value)
        else:
            raise ValueError("Key not found")

    def get(self, key):
        if key in self.declarations:
            return self.declarations[key]
        elif self.closest_env:
            return self.closest_env.get(key)
        else:
            raise SemanticError(f"Unbound variable {key}")
