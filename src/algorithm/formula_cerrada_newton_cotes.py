
# Formulas cerradas comunes de Newton Cotes
from sympy import *

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






