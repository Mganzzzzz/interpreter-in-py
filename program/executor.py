from dataclasses import dataclass

from ast2.object import Program, FunctionCall, Expression, FunctionDecl
from program.buildIn.func import println


@dataclass()
class Executor:
    program: Program

    def exec(self):
        self.dfs()

    def dfs(self):
        for statement in self.program.statement:
            if isinstance(statement, FunctionDecl):
                pass
            elif isinstance(statement, Expression):
                pass
            elif isinstance(statement, FunctionCall):
                self.exec_func_call(statement)

    def is_build_in(self, func: FunctionCall):
        buildInFuncList = [
            'println'
        ]
        return func.funcName.raw in buildInFuncList

    def exec_func_call(self, statement: FunctionCall):
        parameter = statement.functionParameter.parameter
        args = [n.raw for n in parameter]
        if self.is_build_in(statement):
            return println(*args)
        else:
            ref = statement.funcRef
            funcBody = ref.funcBody
            for statement1 in funcBody.statement:
                if isinstance(statement1, FunctionCall):
                    self.exec_func_call(statement1)
