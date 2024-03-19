class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        token = self.current_token()
        if token.type == 'LPAREN':
            return self.parse_list()
        elif token.type == 'NUMBER':
            self.consume_token()
            return token
        elif token.type == 'SYMBOL':
            self.consume_token()
            return token
        else:
            raise SyntaxError('Unexpected token: {}'.format(token.value))

    def parse_list(self):
        self.consume_token()  # Consume '('
        result = []
        while self.current_token().type != 'RPAREN':
            result.append(self.parse_expression())
        self.consume_token()  # Consume ')'
        return result

    def current_token(self):
        return self.tokens[self.current_token_index]

    def consume_token(self):
        self.current_token_index += 1

def lex(code):
    # Пример простого лексического анализатора, который преобразует строку кода в массив токенов
    # Например, для упрощения предполагается, что разделителем является пробел, и скобки обозначаются '(' и ')'
    tokens = []
    for token in code.split():
        if token == '(':
            tokens.append(Token('LPAREN'))
        elif token == ')':
            tokens.append(Token('RPAREN'))
        else:
            try:
                value = int(token)
                tokens.append(Token('NUMBER', value))
            except ValueError:
                tokens.append(Token('SYMBOL', token))
    return tokens

def main():
    code = "(+ 1 (* 2 3))"
    tokens = lex(code)
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)

if __name__ == "__main__":
    main()
