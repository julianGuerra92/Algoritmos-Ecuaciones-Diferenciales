
# Ana Isabel
from sympy import *

class ReglaCompuestaPuntoMedio:

   def __init__(self, funcion, a, b, n):
      self.funcion = sympify(funcion.replace("pi", str(pi)).replace("ln", "log").replace("^", "**").replace("e", str(E)))
      self.a = a
      self.b = b
      self.n = n
      self.x = symbols('x')
      self.h = (b - a) / (n + 2)

   def calcularIntegral(self):
        suma = 0
        j = 0
        for j in range(int(self.n / 2)+1): 
            k = 2 * j
            Xj = self.a + (k + 1) * self.h 
            suma += self.funcion.subs(self.x, Xj) 
        integral = 2 * self.h * suma
        return integral
   
   def calcularError(self):
        m = (self.a + self.b) / 2
        error = (((self.b - self.a)/6) * self.h**2) * diff(self.funcion, self.x, 2).subs(self.x, m)
        return error
   
   def imprimir_resultado(self):
        valor_integral = self.calcularIntegral()
        valor_error = self.calcularError()
        print(f'\nResultado Integral: {valor_integral}')
        print(f'Error: {valor_error}')
        print(f'Resultado con error: {valor_integral + valor_error}')

