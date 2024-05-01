# -*- coding: utf-8 -*-

import pulp
import os


class Linear_program:

    def __init__(self, equation, austerity):
        self.equation = equation
        self.austerity = austerity

    @staticmethod
    def example():
        print("-" * 60)
        print(
            """
            equation = [
                "max = 60 * x + 100 * y",
                "0.18 * x + 0.09 * y <= 72",
                "0.08 * x + 0.28 * y <= 56",
            ]
            
            austerity = [
                ['x', 0, "", 'Continuous'],
                ['y', 0, "", 'Continuous'],
            ]
            """
        )
        print("-" * 60)

    def calculate(self):

        expression = self.equation[0]
        lhs, rhs = expression.split("=")
        lhs = lhs.strip()
        rhs = rhs.strip()

        if lhs == "max":
            MyProbLP = pulp.LpProblem("MyProbLP", sense=pulp.LpMaximize)
        else:
            MyProbLP = pulp.LpProblem("MyProbLP", sense=pulp.LpMinimize)

        variables = {}
        for index in range(len(self.austerity)):
            if self.austerity[index][1] == "":
                if self.austerity[index][2] == "":
                    variables[self.austerity[index][0]] = pulp.LpVariable(self.austerity[index][0],
                                                                          lowBound=None,
                                                                          upBound=None,
                                                                          cat=self.austerity[index][3])
                else:
                    variables[self.austerity[index][0]] = pulp.LpVariable(self.austerity[index][0],
                                                                          lowBound=None,
                                                                          upBound=float(self.austerity[index][2]),
                                                                          cat=self.austerity[index][3])
            elif self.austerity[index][2] == "":
                variables[self.austerity[index][0]] = pulp.LpVariable(self.austerity[index][0],
                                                                      lowBound=float(self.austerity[index][1]),
                                                                      upBound=None,
                                                                      cat=self.austerity[index][3])
            else:
                print("austerity error")

        objective = eval(rhs, variables)
        MyProbLP += objective

        for index in range(1, len(self.equation)):
            MyProbLP += eval(self.equation[index], variables)

        original_stdout = os.dup(1)
        temp_fd = os.open(os.devnull, os.O_WRONLY)
        os.dup2(temp_fd, 1)

        try:
            MyProbLP.solve()

        except Exception as e:
            print(
                f"This is an error {e}, but the most likely is an input error."
            )

        os.dup2(original_stdout, 1)
        os.close(original_stdout)

        print(pulp.LpStatus[MyProbLP.status])
        for var in MyProbLP.variables():
            print(f"{var.name}: {var.varValue}")
        print(f"Objective: {pulp.value(MyProbLP.objective)}")