from lexer import Lexer
from parse import Parser
from interpreter import Interpreter

while True:
    text = input('SoKeR: ')

    #Lexical Analysis
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    #Parsing
    parser = Parser(tokens)
    tree = parser.parse()

    #Interpretation
    interpreter = Interpreter(tree)
    result = interpreter.interpret()

    print(result)