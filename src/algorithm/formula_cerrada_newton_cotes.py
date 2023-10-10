
# Formulas cerradas comunes de Newton Cotes
from sympy import *

class FormulasCerradasNewtonCotes:

        def __init__(self, funcion, a, b):
            self.funcion = sympify(funcion.replace("pi", str(pi)).replace("^", "**"))
            self.a = float(a)
            self.b = float(b)
            self.x = symbols('x')

        def regla_tres_octavos_Simpson(self):
            h = (self.b - self.a) / 3  
            x1 = self.a + h
            x2 = x1 + h
            
            integral = (3 * h / 8) * (self.funcion.subs(self.x, self.a) + 3*(self.funcion.subs(self.x, x1))+ 3*(self.funcion.subs(self.x, x2))+ self.funcion.subs(self.x,self.b))

            error = (3 * h**5 / 80) * diff(self.funcion, self.x, 4).subs(self.x, (self.b+ x2+ x1+ self.a)/4)
            return integral - error

        def regla_Simpson(self):
            h = (self.b - self.a) / 2 
            x1 = self.a + h

            integral = (h/3)*(self.funcion.subs(self.x,self.a) + 4*(self.funcion.subs(self.x, x1)) + (self.funcion.subs(self.x, self.b)))

            error = h**5/90* diff(self.funcion, self.x, 4).subs(self.x, (self.b + x1 + self.a)/3)
            return integral - error
        
        def regla_del_trapecio(self):
            h = (self.b - self.a)

            integral = (h/2)*(self.funcion.subs(self.x, self.a) + self.funcion.subs(self.x, self.b)) 
            error = h**3/12* diff(self.funcion, self.x, 2).subs(self.x, (self.a+ self.b)/2)
            return integral - error

        def imprimir_resultado(self):
            resultado_regla_del_trapecio = self.regla_del_trapecio()
            resultado_regla_Simpson = self.regla_Simpson()
            resultado_tres_octavos_Simpson = self.regla_tres_octavos_Simpson()
            print(f'El resultado con la regla del trapecio es: {resultado_regla_del_trapecio}')
            print(f'El resultado con la regla de Simpson es: {resultado_regla_Simpson}')
            print(f'El resultado con la regla de 3/8 de Simpson es: {resultado_tres_octavos_Simpson}')
            





"""

x = symbols('x')
x0 = float(input("Ingrese el primer limite de integración: "))
x1 = float(input("Ingrese el otro limite de integración: "))
funcion = eval(input("Ingrese la función (ejm: x^2, pi/4): ").replace("pi", str(pi)).replace("^", "**"))

ht = x1 - x0
trapecio = (ht/2)*(funcion.subs(x,x0)+funcion.subs(x, x1)) - ht**3/12* diff(funcion, x, 2).subs(x, (x0+x1)/2)
print("El resultado con la regla del trapecio es: " + str(trapecio))

x2 = float(input("Ingrese el otro limite de integración: "))
hs = (x2-x0)/2
simpson = (hs/3)*(funcion.subs(x,x0)+4*(funcion.subs(x, x1))+(funcion.subs(x, x2))) - hs**5/90* diff(funcion, x, 4).subs(x, (x2+x1+x0)/3)

x3 = float(input("Ingrese el otro limite de integración: "))
hsm = (x3-x0)/3
simpson = (3*hsm/8)*(funcion.subs(x,x0) + 3*(funcion.subs(x, x1))+3*(funcion.subs(x, x2))+ funcion.subs(x,x3))- (3* (hsm**5)/80) * diff(funcion, x, 4).subs(x, (x3+x2+x1+x0)/4)


"""



