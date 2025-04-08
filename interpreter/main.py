import sys

from parser import Parser
from environment import Environment
from interpreter import execute
from lexer import Lexer

def main():
    if len(sys.argv) != 2:
            print(f"Usage: {sys.argv[0]} <filename.i>")
            sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as file:
        code = file.read()
    
    lexer = Lexer(code)

    # token = lexer.scan()
    # while token.tag != 'EOF':
    #     print(token)
    #     token = lexer.scan() 

    parser = Parser(lexer)

    instructions = parser.parse()

    # for instr in instructions:
    #     print(instr.__class__.__name__, vars(instr))

    env = Environment(instructions)
    execute(env)

    print("Final memory state:", env.memory)

if __name__ == "__main__":
    main()
