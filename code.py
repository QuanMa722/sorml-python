from sorml import Linear_program
from sorml import Chart


equation = [
    "max = 60 * x + 100 * y",
    "0.18 * x + 0.09 * y <= 72",
    "0.08 * x + 0.28 * y <= 56",
]

austerity = [
    ['x', 0, "", 'Continuous'],
    ['y', 0, "", 'Continuous'],
]

linear_program = Linear_program(equation, austerity)
linear_program.calculate()
