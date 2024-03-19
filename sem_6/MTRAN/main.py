from Token_type import *
from const import *
from Token import *
from Lexer import Lexer
from utils import *

def main():
 
    with open('C:\\D\BSUIR\\sem_6\\MTRAN\\input.txt', 'r', encoding='utf-8') as f:
        code = f.read()
    
    print('\n', code, '\n')
    lexer = Lexer(code)
    brackets_balanced, error_position = lexer.check_brackets()

    if not brackets_balanced:
        display_error(code, error_position)
   
    result = get_token_table(code) 
    print(result[0])
    print(result[1])

if __name__ == "__main__":
    main()

