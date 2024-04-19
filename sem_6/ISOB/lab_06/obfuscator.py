import os
import random
import re
import string

VAR_NAMES = {}
NOT_NAMES = [
    "import",
    "sqlite3",
    "def",
    "config",
    "connect",
    "conn",
    "cursor",
    "commit",
    "execute",
    "fetchall",
    "executemany",
    "not",
    "close",
    "if",
    "tkinter",
    "tk",
    "class",
    "Entry",
    "__init__",
    "None",
    "self",
    "True",
    "kwargs",
    "super",
    "bind",
    "get",
    "and",
    "len",
    "delete",
    "END",
    "return",
    "list",
    "in",
    "for",
    "str",
    "join",
    "from",
    "as",
    "range",
    "Protected_entry",
    "protected_entry",
    "bd_config",
    "geometry",
    "title",
    "requests",
    "f",
    "else",
    "wraplength",
    "text",
    "pass",
    "main",
    "__name__",
    "destroy",
    "False",
    "Toplevel",
    "messagebox",
]

def get_cmp_sign(lhs, rhs):
    if lhs == rhs:
        return random.choice(["==", ">=", "<="])
    elif lhs > rhs:
        return random.choice(["!=", ">=", ">"])
    else:
        return random.choice(["!=", "<=", "<"])

def get_opposite_cmp_sign(lhs, rhs):
    if lhs == rhs:
        return "!="
    elif lhs > rhs:
        return "<"
    else:
        return ">"

def generate_expr(nested=False, level=0, max_level=3):
    if not nested or level > max_level:
        return str(random.randint(0, 12344))
    else:
        nested1 = random.choice([True, False])
        nested2 = random.choice([True, False])
        operators = ["+", "-", "*"]
        return f"({generate_expr(nested1, level + 1)} {random.choice(operators)} {generate_expr(nested2, level + 1)})"

def generate_assignment(var):
    return f"{var} = {generate_expr(True)}"

def generate_dead_code():
    result = generate_expr() + "\n"
    result += generate_assignment(generate_random_name(5)) + "\n"
    return result

def rename_vars(code):
    def replace(match):
        var_name = match.group(1)
        if var_name in NOT_NAMES: 
            return match.group(0)
        if var_name not in VAR_NAMES:
            VAR_NAMES[var_name] = generate_random_name(10)
        return VAR_NAMES[var_name]
    
    pattern = r"(?<![<#\/])(?=(?:[^\"']|\"[^\"]*\"|'[^']*')*$)\b([a-zA-Z_][a-zA-Z_0-9]*)\b(?![<>])"
    return re.sub(pattern, replace, code)

def generate_random_name(length):
    possible_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    random_name = ''.join(random.choice(possible_chars) for _ in range(length))
    while random_name in VAR_NAMES:
        random_name = ''.join(random.choice(possible_chars) for _ in range(length))
    return random_name

def replace_numbers(code):
    def replace(match):
        number = int(match.group(1))
        result = ""
        cur = 0
        rem = number + 1
        max_op_cnt = random.randint(2, 5)
        while cur != number:
            if max_op_cnt == 0:
                result += f"0x{rem - 1:x} + "
                break
            tmp = random.randint(0, rem - 1)
            result += f"0x{tmp:x} + "
            cur += tmp
            rem -= tmp
            max_op_cnt -= 1
        result += "0x0"
        return "(" + result + ")"
    pattern = r"(?<!\.)\b(\d+)\b(?!\.)"
    return re.sub(pattern, replace, code)

def replace_strings(code):
    def replace(match):
        string = match.group(0)
        unicode_string = ''.join(['\\u{:04x}'.format(ord(char)) for char in string])
        return f'u"{unicode_string}"'
    
    pattern = r'"(?:[^"\\]|\\.)*"'
    return re.sub(pattern, replace, code)

def generate_junk_code():
    junk_code = ""
    num_lines = random.randint(5, 15)
    for _ in range(num_lines):
        junk_code += generate_assignment(generate_random_name(5)) + "\n"
    return junk_code


def obfuscate(code):
    result = rename_vars(code)
    result = replace_strings(result)
    result = replace_numbers(result)
    result += generate_junk_code()

    return result

def get_file_names(data_dir):
    file_names = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith((".py")):
                file_names.append(os.path.abspath(os.path.join(root, file)))
    return file_names

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    return code

def main():
    file_names = get_file_names("lab_04_05")
    for file_name in file_names:
        code = read_file(file_name)
        obfuscated_code = obfuscate(code)
        to_replace = "lab_04_05"
        replace_with = "lab_04_05_copy"
        out_path = file_name.replace(to_replace, replace_with)
        with open(out_path, 'w') as out:
             out.write(obfuscated_code)
        os.system("clang-format -i " + out_path)

if __name__ == "__main__":
    main()
