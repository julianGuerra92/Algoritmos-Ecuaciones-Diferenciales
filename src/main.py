
import numpy as np

from algorithm.formula_progresiva import FormulaProgresiva
from algorithm.formula_central import FormulaCentral
from algorithm.formula_cinco_puntos import FormulaCincoPuntos
from algorithm.diferencias_divididas import DiferenciasDivididas
from algorithm.compuesta_simpsons import ReglaCompuestaSimpsons

'''
print("Resultado fórmula Progresiva:")
resultado_formula_progresiva = FormulaProgresiva("cos(x)", 0.785398163)
resultado_formula_progresiva.imprimir_tabla()

print("Resultado fórmula Central:")
resultado_formula_central = FormulaCentral("ln(x)", 1.8)
resultado_formula_central.imprimir_tabla()

print("Resultado fórmula Cinco Puntos:")
resultado_formula_cinco_puntos = FormulaCincoPuntos("cos(x)", np.pi/4)
resultado_formula_cinco_puntos.imprimir_tabla()

'''

print("Resultado algoritmo diferencias divididas:")
#xi = np.array(input("Ingrese los valores de xi: ").split(), dtype=float)
#fi = np.array(input("Ingrese los valores de fi: ").split(), dtype=float)
xi = np.array([1, 1.3, 1.6, 1.9, 2.2], dtype=float)
fi = np.array([0.7651, 0.6200, 0.4554, 0.2818, 0.1103], dtype=float)

resultado_diferencias_divididas = DiferenciasDivididas(xi, fi)
resultado_diferencias_divididas.imprimir_tabla()


print("Resultado algoritmo compuesta simpsons:")
resultado_compuesta_simpsons = ReglaCompuestaSimpsons("x*ln(x)", 1, 2, 4)
resultado_compuesta_simpsons.imprimir_resultado()