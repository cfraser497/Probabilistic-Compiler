import argparse

from parser import Parser
from interpreter import Environment
from interpreter import Executor
from lexer import Lexer
from pcfgbuilder import PCFGBuilder

def main():
    argparser = argparse.ArgumentParser(description="Run interpreter on input file.")
    argparser.add_argument("filename", help="Path to the .i file to run.")
    argparser.add_argument("--seed", type=int, help="Optional random seed for reproducibility.")
    argparser.add_argument("--pcfg", action="store_true", help="Optional to generate a PCF")

    args = argparser.parse_args() 

    with open(args.filename, 'r') as file:
        code = file.read()
    
    lexer = Lexer(code)

    # token = lexer.scan()
    # while token.tag != 'EOF':
    #     print(token)
    #     token = lexer.scan() 
    # lexer = Lexer(code)
    
    parser = Parser(lexer)

    instructions, variables = parser.parse()

    env = Environment(instructions, variables)
    
    executor = Executor(env, seed=args.seed)
    executor.run()

    # for name, info in variables.items():
        # print(f"{name}: {info}")
    # 
    # for instr in instructions:
        # print(instr)

    print("Final memory state:")

    for k, v in env.memory.items():
        print(f"{k}: {v}")

    if args.pcfg:
        cfg = PCFGBuilder(instructions, env.labels)
        cfg.build()
        cfg.visualize("pcfg.png")

if __name__ == "__main__":
    main()
