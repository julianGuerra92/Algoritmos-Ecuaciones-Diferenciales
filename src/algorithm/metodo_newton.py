
# Metodo de newton o newton rapshon

from sympy import *
class MetodoNewton:

        def __init__(self, funcion, po, tol, NoIteraciones):
            self.funcion = sympify(funcion)
            self.po = eval(po.replace("pi", str(pi)))
            self.tol = float(tol)
            self.NoIteraciones = int(NoIteraciones)
            self.x = symbols('x')

        def metodo_newton(self):
            i = 1
            while i <= self.NoIteraciones:
                p = self.po - (self.funcion.subs(self.x, self.po) / diff(self.funcion, self.x).subs(self.x, self.po))
                if abs(p - self.po) < self.tol:
                    return str(p.evalf())
                    break    
                i = i + 1
                self.po = p    
            else:
                return None

        def imprimir_resultado(self):
            resultado = self.metodo_newton()
            if resultado == None:
                print(f'El método de Newton-Raphson no convergió después de {self.NoIteraciones} iteraciones.')
            else:
                print(f'La raiz aproximada es: {resultado}')
            
