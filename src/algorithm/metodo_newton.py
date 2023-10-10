
# Metodo de newton o newton rapshon

from sympy import *

x = symbols('x')
funcion = eval(input("Ingrese aquí la funcion: "))
po = eval(input("Ingresa el valor inicial: ").replace("pi", str(pi)))
tol = float(input("Ingresa el nivel de tolerancia o error: "))
NoIteraciones = int(input("Ingresa el numero maximo de iteraciones: "))
i = 1

while i <= NoIteraciones:
    p = po - (funcion.subs(x, po) / diff(funcion, x).subs(x, po))
    if abs(p - po) < tol:
        print("La raiz aproximada es: " + str(p.evalf()))
        break    
    i = i + 1
    po = p    
else:
    print("El método de Newton-Raphson no convergió después de", NoIteraciones, "iteraciones.")

