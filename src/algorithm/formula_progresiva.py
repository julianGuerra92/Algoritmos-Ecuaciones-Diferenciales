
# Julian

from sympy import *
from tabulate import tabulate
import sympy as sp
import numpy as np

init_printing(use_unicode=True)

class FormulaProgresiva:

    def __init__(self, expression, value):
        self.expression = expression
        self.value = value
        self.x = symbols('x')
        self.y = symbols('y')
        self.epsilon = np.logspace(-1, -4, 4, base=10)

    def calculate_derivate_numeric(self):
        exp = sp.sympify(self.expression)
        funcion_numeric = sp.lambdify(self.x, exp, 'numpy')
        derivada_numerica = (funcion_numeric(self.value + self.epsilon) - funcion_numeric(self.value)) / self.epsilon
        return derivada_numerica

    def calculate_derivative(self):
        return diff(self.expression, self.x, 2)

    def calculate_error(self):
        derivada = self.calculate_derivative()
        funcion_numeric = sp.lambdify(self.x, derivada, 'numpy')
        error = abs((self.epsilon / 2)*funcion_numeric(self.value))
        return error
    
    def imprimir_tabla(self):
        data = list(zip(self.epsilon, self.calculate_derivate_numeric(), self.calculate_error()))
        tabla = tabulate(data, headers=['Epsilon', 'Derivada numérica', 'Error'], tablefmt='fancy_grid')
        print(tabla)
