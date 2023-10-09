
# Julian
from sympy import *
import sympy as sp
import numpy as np



class ReglaCompuestaSimpsons:

   def __init__(self, expression, a, b, n):
      self.expression = expression
      self.a = a
      self.b = b
      self.n = n
      self.x = symbols('x')
      self.h = (b - a) / n

   def calcularIntegral(self):
      exp = sp.sympify(self.expression)
      funcion_numeric = sp.lambdify(self.x, exp, 'numpy')
      suma = 0
      array_x = np.zeros(shape=(self.n + 1))
      array_x[0] = self.a

      for j in range(1, self.n + 1):
         array_x[j] = self.a + (j * self.h)
      
      for j in range(1, (self.n//2) + 1):
         print(suma)
         suma += ((funcion_numeric(array_x[2*j - 2])) + (4*funcion_numeric(array_x[2*j - 1])) + (funcion_numeric(array_x[2*j])))

      return (self.h/3)*suma
   
   def calcularError(self):
      exp = sp.sympify(self.expression)
      derivada = diff(exp, self.x, 4)
      funcion_numeric_derivada = sp.lambdify(self.x, derivada, 'numpy')
      return abs(((self.b - self.a)/180)*(self.h**4)*(funcion_numeric_derivada((self.a + self.b) / 2 )))

   def imprimir_resultado(self):
      valor_integral = self.calcularIntegral()
      valor_error = self.calcularError()
      print(f'\nResultado Integral: {valor_integral}')
      print(f'Error: {valor_error}')
      print(f'Resultado con error: {valor_integral - valor_error}')

         

      
