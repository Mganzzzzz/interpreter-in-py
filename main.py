from ast2.parser import AstParser
from program.executor import Executor
from tokenizer import Tokenizer

if __name__ == '__main__':
    with open('source.txt') as f:
        content = f.read()
        tokenizer = Tokenizer(content)
        tokens = tokenizer.parse()
        print(tokens)
        ast = AstParser(tokenList=tokens)
        astTree = ast.parse_program()
        print(astTree)
        programExec = Executor(astTree)
        programExec.exec()
