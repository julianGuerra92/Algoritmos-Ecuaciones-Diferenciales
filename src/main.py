
import numpy as np

from algorithm.formula_progresiva import FormulaProgresiva
from algorithm.formula_central import FormulaCentral
from algorithm.formula_cinco_puntos import FormulaCincoPuntos
from algorithm.diferencias_divididas import DiferenciasDivididas
from algorithm.compuesta_simpsons import ReglaCompuestaSimpsons
from algorithm.trapecio_compuesta import ReglaTrapecioCompuesta
from algorithm.metodo_newton import *
from algorithm.formula_cerrada_newton_cotes import *
from algorithm.compuesta_punto_medio import ReglaCompuestaPuntoMedio

menu = '''
      -- Métodos Numéricos --
      1. Fórmula Progresiva
      2. Fórmula Central
      3. Fórmula Cinco Puntos
      4. Algoritmo Diferencias Divididas
      5. Algoritmo Compuesta Simpson
      6. Algoritmo Trapecio Compuesta
      7. Compuesta Punto Medio
      8. Método Newton
      9. Fórmula cerrada de Newton-Cotes
      0. Salir
      '''
print(menu)
opcion = int(input("Ingrese la opción deseada: "))

while opcion != 0:

   if(opcion == 1):
      funcion = input("Ingrese la función: ")
      valor = float(input("Ingrese el valor a evaluar: "))
      resultado_formula_progresiva = FormulaProgresiva(funcion, valor)
      resultado_formula_progresiva.imprimir_tabla()
      input("Presione enter para continuar...")

   elif(opcion == 2):
      funcion = input("Ingrese la función: ")
      valor = float(input("Ingrese el valor a evaluar: "))
      resultado_formula_central = FormulaCentral(funcion, valor)
      resultado_formula_central.imprimir_tabla()
      input("Presione enter para continuar...")

   elif(opcion == 3):
      funcion = input("Ingrese la función: ")
      valor = float(input("Ingrese el valor a evaluar: "))
      resultado_formula_cinco_puntos = FormulaCincoPuntos(funcion, valor)
      resultado_formula_cinco_puntos.imprimir_tabla()
      input("Presione enter para continuar...")

   elif(opcion == 4):
      xi = np.array(input("Ingrese los valores de xi: ").split(), dtype=float)
      fi = np.array(input("Ingrese los valores de fi: ").split(), dtype=float)
      resultado_diferencias_divididas = DiferenciasDivididas(xi, fi)
      resultado_diferencias_divididas.imprimir_tabla()
      input("Presione enter para continuar...")

   elif(opcion == 5):
      funcion = input("Ingrese la función: ")
      a = float(input("Ingrese el valor de a: "))
      b = float(input("Ingrese el valor de b: "))
      n = int(input("Ingrese el valor de n: "))
      resultado_compuesta_simpsons = ReglaCompuestaSimpsons(funcion, a, b, n)
      resultado_compuesta_simpsons.imprimir_resultado()
      input("Presione enter para continuar...")

   elif(opcion == 6):
      funcion = input("Ingrese la función: ")
      a = float(input("Ingrese el valor de a: "))
      b = float(input("Ingrese el valor de b: "))
      n = int(input("Ingrese el valor de n: "))
      resultado_trapecio_compuesta = ReglaTrapecioCompuesta(funcion, a, b, n)
      resultado_trapecio_compuesta.imprimir_resultado()
      input("Presione enter para continuar...")

   elif(opcion == 7):
      print("Compuesta Punto Medio")
      funcion = input("Ingrese la función: ")
      a = float(input("Ingrese el valor de a: "))
      b = float(input("Ingrese el valor de b: "))
      n = int(input("Ingrese el valor de n: "))
      resultado_compuesta_punto_medio = ReglaCompuestaPuntoMedio(funcion, a, b, n)
      resultado_compuesta_punto_medio.imprimir_resultado()
      input("Presione enter para continuar...")
   
   elif(opcion == 8):
      print("Método Newton")
      funcion = input("Ingrese aquí la funcion: ")
      po = input("Ingresa el valor inicial: ")
      tol = float(input("Ingresa el nivel de tolerancia o error: "))
      NoIteraciones = int(input("Ingresa el numero maximo de iteraciones: "))
      resultado_metodo_newton = MetodoNewton(funcion, po, tol, NoIteraciones)
      resultado_metodo_newton.imprimir_resultado()

      input("Presione enter para continuar...")

   elif(opcion == 9):
      print("Fórmulas cerradas de Newton-Cotes")
      a = float(input("Ingrese el valor de a: "))
      b = float(input("Ingrese el valor de b: "))
      funcion = input("Ingrese la función (ejm: x^2, pi/4): ")
      resultado_formulas_cerradas = FormulasCerradasNewtonCotes(funcion, a, b)
      resultado_formulas_cerradas.imprimir_resultado()
      input("Presione enter para continuar...")
   
   else:
      print("Opción inválida")
      input("Presione enter para continuar...")

   print(menu)
   opcion = int(input("Ingrese la opción deseada: "))

print("Fin del programa")

