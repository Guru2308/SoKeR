from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data
db = Data()

while True:
    text = input('SoKeR: ')

    #Lexical Analysis
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    print(tokens)
    #Parsing
    parser = Parser(tokens)
    tree = parser.parse() 
    print(tree)
    # Interpretation
    interpreter = Interpreter(tree,db)
    result = interpreter.interpret()

    print(result)