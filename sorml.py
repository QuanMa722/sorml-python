from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pulp
import os


class Data_process:
    ...


class Linear_program:

    def __init__(self, equation, austerity):
        self.equation = equation
        self.austerity = austerity

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


class Chart:

    def __init__(self, file):
        self.file = file

    def scatter(self, item_list, dimension):
        try:
            try:
                data = pd.read_csv(self.file, encoding="utf-8")
            except UnicodeDecodeError:
                data = pd.read_csv(self.file, encoding="gbk")
            except FileNotFoundError:
                print("File not found")
                return

            if dimension == 2:

                if len(item_list) == 1:
                    print("Input error!")
                else:
                    data_x = data[item_list[0]]
                    data_y = data[item_list[1:]]

                    for column in data_y.columns:
                        plt.scatter(data_x, data_y[column], label=column)

                    plt.title('Scatter Plot')
                    plt.xlabel('X-axis label')
                    plt.ylabel('Y-axis label')
                    plt.legend()
                    plt.grid()
                    plt.show()

            elif dimension == 3:
                ...

        except Exception as e:
            print(f"An error occurred: {e}")

    # def plot(self):


class Statistic:

    def __init__(self, file):
        self.file = file

    def average(self, column):
        try:
            if isinstance(column, list):
                column_array = np.array(column)
                average_value = np.mean(column_array)
                return average_value
            else:
                try:
                    data = pd.read_csv(self.file, encoding="utf-8")
                except UnicodeDecodeError:
                    data = pd.read_csv(self.file, encoding="gbk")
                except FileNotFoundError:
                    print("File not found")
                    return

                column_array = np.array(data[column])
                average_value = np.mean(column_array)
                return average_value

        except Exception as e:
            print(f"An error occurred: {e}")

    def variance(self, column):
        try:
            if isinstance(column, list):
                column_array = np.array(column)
                variance_value = np.var(column_array)
                return variance_value
            else:
                try:
                    data = pd.read_csv(self.file, encoding="utf-8")
                except UnicodeDecodeError:
                    data = pd.read_csv(self.file, encoding="gbk")
                except FileNotFoundError:
                    print("File not found")
                    return

                column_array = np.array(data[column])
                variance_value = np.var(column_array)
                return variance_value

        except Exception as e:
            print(f"An error occurred: {e}")

    def max(self, column):
        try:
            if isinstance(column, list):
                max_value = max(column)
                return max_value
            else:
                try:
                    data = pd.read_csv(self.file, encoding="utf-8")
                except UnicodeDecodeError:
                    data = pd.read_csv(self.file, encoding="gbk")
                except FileNotFoundError:
                    print("File not found")
                    return

                column_array = np.array(data[column])
                max_value = np.max(column_array)
                return max_value

        except Exception as e:
            print(f"An error occurred: {e}")

    def min(self, column):
        try:
            if isinstance(column, list):
                min_value = min(column)
                return min_value
            else:
                try:
                    data = pd.read_csv(self.file, encoding="utf-8")
                except UnicodeDecodeError:
                    data = pd.read_csv(self.file, encoding="gbk")
                except FileNotFoundError:
                    print("File not found")
                    return

                column_array = np.array(data[column])
                min_value = np.min(column_array)
                return min_value

        except Exception as e:
            print(f"An error occurred: {e}")

    def median(self, column):
        try:
            if isinstance(column, list):
                median_value = np.median(column)
                return median_value
            else:
                try:
                    data = pd.read_csv(self.file, encoding="utf-8")
                except UnicodeDecodeError:
                    data = pd.read_csv(self.file, encoding="gbk")
                except FileNotFoundError:
                    print("File not found")
                    return

                column_array = np.array(data[column])
                median_value = np.median(column_array)
                return median_value

        except Exception as e:
            print(f"An error occurred: {e}")
