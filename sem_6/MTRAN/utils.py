import re
from tabulate import tabulate
from Token_type import *
from const import *
from Token import *
from utils import *

def display_error(code, error_position):
    line, column = get_line_and_column_skob(code, error_position)

    print("Ошибка в расстановке скобок:")
    for i, line_text in enumerate(code.splitlines(), start=1):
        print(f"{i}: {line_text}")
        if i == line:
            indicator = ' ' * column + '^'
            print(f"   {indicator}")

    print(f"Позиция ошибки: строка {line}, столбец {column + 1}.")  

def get_line_and_column_skob(text, position):
    lines = text.splitlines()
    line_start = 0
    for i, line in enumerate(lines, start=1):
        line_end = line_start + len(line)
        if line_start <= position <= line_end:
            column = position - line_start
            return i, column
        line_start = line_end + 1  
    return -1, -1 

def is_similar_by_one_letter(word1, word2):
    if abs(len(word1) - len(word2)) > 1:
        return False
    if word1 == '#f':
        return False

    if len(word1) < len(word2):
        word1, word2 = word2, word1

    differences = 0
    index2 = 0

    for index1 in range(len(word1)):
        if index2 >= len(word2) or word1[index1] != word2[index2]:
            differences += 1
            if len(word1) == len(word2):
                index2 += 1
        else:
            index2 += 1

        if differences > 1:
            break

    return differences <= 1

def find_similar_word(input_word, word_list):
    similar_words = [word for word in word_list if is_similar_by_one_letter(input_word, word)]

    return similar_words

def get_line_and_column(string, position):
    line = 1
    column = 1

    for i in range(position):
        if string[i] == '\n':
            line += 1
            column = 1
        else:
            column += 1

    return line, column

def get_token_type(token, token_types):
    for key, value in token_types.items():
        pattern = value.regex
        if re.fullmatch(pattern, token):
            return value
    return None

def get_token_table(code):
    errors = 0
    tokens = []
    specialCharsPattern = r"(~@|[\[\]{}(),~@])"
    stringPattern = r'""(?:[\\].|[^\\""])*""?'
    commentPattern = r';.*'
    otherPattern = r"[^\s \[\]{}()""~@;]*"
    combined_pattern = f"({specialCharsPattern}|{stringPattern}|{commentPattern}|{otherPattern})"

    regex = re.compile(combined_pattern)
    table_data = []
    tokens = []
    lexems = []
    for match in regex.finditer(code):
        token = match.group(1)
        position = match.start()
        line, column = get_line_and_column(code, position)
        if token and token[0] != ';': 
            token_type = get_token_type(token, TOKEN_TYPES) 
            t = Token(token, token_type, position)
            tokens.append(t)
            lexems.append(t.name)
            table_data.append([t.name, t.type.name if t.type else "Unknown", line, column])
            if token not in KEY_WORDS:
                    similar_words = [word for word in find_similar_word(token, KEY_WORDS.keys()) if word != token]
                    if similar_words:
                        print(f"ОШИБКА '{token}': {', '.join(similar_words)}")
                        errors = 1
            if not t.type:
                    print(f"ОШИБКА '{t.name}': Unknown type")
                    errors = 1

    if tokens[0].name !='(':
        print(f"ОШИБКА '{tokens[0].name}': Код должен начинаться с символа '('")
        errors = 1
    elif tokens[len(tokens)-1].name != ')':
        print(f"ОШИБКА '{tokens[len(tokens)-1].name}': Код должен заканчиваться символом ')'")
        errors = 1
    headers = ["Token", "Type", "Line", "Column"]
    

    return errors, (tabulate(table_data, headers=headers)), lexems