
from algorithm.formula_progresiva import FormulaProgresiva
from algorithm.formula_central import FormulaCentral

print("Resultado fórmula Progresiva:")
resultado_formula_progresiva = FormulaProgresiva("ln(x)", 1.8)
resultado_formula_progresiva.imprimir_tabla()

print("Resultado fórmula Central:")
resultado_formula_central = FormulaCentral("ln(x)", 1.8)
resultado_formula_central.imprimir_tabla()