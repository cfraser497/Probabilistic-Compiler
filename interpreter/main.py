import argparse

from parser import Parser
from environment import Environment
from interpreter import execute
from lexer import Lexer

def main():
    argparser = argparse.ArgumentParser(description="Run interpreter on input file.")
    argparser.add_argument("filename", help="Path to the .i file to run.")
    argparser.add_argument("--seed", type=int, help="Optional random seed for reproducibility.")

    args = argparser.parse_args() 

    with open(args.filename, 'r') as file:
        code = file.read()
    
    lexer = Lexer(code)

    # token = lexer.scan()
    # while token.tag != 'EOF':
    #     print(token)
    #     token = lexer.scan() 

    parser = Parser(lexer)

    instructions = parser.parse()

    for instr in instructions:
        print(instr.__class__.__name__, vars(instr))

    env = Environment(instructions)
    execute(env, args.seed)

    print("Final memory state:")

    for k, v in env.memory.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
