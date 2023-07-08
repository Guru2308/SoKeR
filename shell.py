from lexer import Lexer

while True:
    text = input('SoKeR: ')
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    print(tokens)