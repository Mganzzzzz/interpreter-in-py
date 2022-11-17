from ast2.parser import AstParser
from program.executor import Executor
from tokenizer import Tokenizer

if __name__ == '__main__':
    with open('source.txt') as f:
        content = f.read()
        tokenizer = Tokenizer(content)
        tokenizer.parse()
        ast = AstParser(tokenizer)
        astTree = ast.parse_program()
        programExec = Executor(astTree)
        programExec.exec()
