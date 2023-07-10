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

    #Parsing
    parser = Parser(tokens)
    tree = parser.parse() 

    # Interpretation
    interpreter = Interpreter(tree,db)
    result = interpreter.interpret()
    
    if result is not None:
        print(result)