

from sorml import Linear_program


austerity = [
    ['x1', 1, "", 'Continuous'],
    ['x2', 1, "", 'Continuous'],
]

equation = [
    "max = 40 * x1 + 30 * x2",
    "x1 + x2 <= 6",
    "240 * x1 + 120 * x2 <= 1200",
]

linear_program = Linear_program(austerity, equation)
linear_program.calculate()
