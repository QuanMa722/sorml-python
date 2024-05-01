import pulp
import sys
import re


class Linear_program:

    def __init__(self, austerity, equation):
        self.austerity = austerity
        self.equation = equation

    @staticmethod
    def parameter_description():

        print("""
        If unconstrained, fill in "", if constrained, fill in the number.
        
        austerity = [
            ['x1', 0, 3, 'Continuous'],
            ['x2', 0, 2, 'Continuous'],
        ]

        equation = [
            "max = 3 * x1 + 4 * x2",
            "2 * x1 + x2 <= 40",
            "x1 + 3 * x2 <= 30",
        ]
        
        """)

    def calculate(self):

        expression = self.equation[0]
        pattern = re.compile(r'(\w+)\s*=\s*(.*)')
        match = pattern.match(expression)
        lhs = match.group(1)
        rhs = match.group(2)

        if lhs == "max":
            MyProbLP = pulp.LpProblem("LPProbDemo1", sense=pulp.LpMaximize)
        else:
            MyProbLP = pulp.LpProblem("LPProbDemo1", sense=pulp.LpMinimize)

        # 创建变量
        variables = {}
        for index in range(len(self.austerity)):
            # 修正这里
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
                variables[self.austerity[index][0]] = pulp.LpVariable(self.austerity[index][0],
                                                                      lowBound=float(self.austerity[index][1]),
                                                                      upBound=float(self.austerity[index][2]),
                                                                      cat=self.austerity[index][3])

        objective = eval(rhs, variables)
        MyProbLP += objective

        for index in range(1, len(self.equation)):
            MyProbLP += eval(self.equation[index], variables)

        try:
            MyProbLP.solve()

        except Exception as e:
            print(
                f"This is an error {e}, but the most likely is an input error."
            )

        if pulp.LpStatus[MyProbLP.status] == "Infeasible":
            print("No solution!")
            sys.exit()

        else:
            for v in MyProbLP.variables():
                print(v.name, "=", v.varValue)

            print("max =", pulp.value(MyProbLP.objective))