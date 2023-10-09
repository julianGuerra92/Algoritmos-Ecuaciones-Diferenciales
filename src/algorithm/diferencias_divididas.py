
# Julian
import numpy as np
import sympy as sp
from tabulate import tabulate


class DiferenciasDivididas:

   def __init__(self, xi, fi):
      self.xi = xi
      self.fi = fi
      self.n = len(xi)
      self.i = np.arange(0, self.n, 1)
      self.dif_div = np.zeros(shape=(self.n, self.n-1), dtype=float)
      self.titulo_tabla = ['i', 'xi', 'fi']

   def calcular_dif_div(self):
      diagonal = 0
      j = 0
      while (j < self.n):
         self.titulo_tabla.append(f'f{j+1}')
         i = self.n - 1
         while (i > diagonal):
            if (j == 0):
               numerador = self.fi[i] - self.fi[i-1]
               denominador = self.xi[i] - self.xi[i-1-diagonal]
            else:
               numerador = self.dif_div[i][j-1] - self.dif_div[i-1][j-1]
               denominador = self.xi[i] - self.xi[i-1-diagonal]
            self.dif_div[i][j] = numerador / denominador
            i -= 1
         diagonal += 1
         j += 1

   def generar_polionomio(self):
      x = sp.Symbol('x')
      polinomio = self.fi[0]
      for i in range(1, self.n):
         termino = self.dif_div[i][i-1]
         for j in range(0, i):
            termino *= (x - self.xi[j])
         polinomio += termino
      return polinomio
       
   def imprimir_tabla(self):
      self.calcular_dif_div()
      data = list(zip(self.i, self.xi, self.fi, *self.dif_div.transpose()))
      tabla = tabulate(data, headers=self.titulo_tabla, tablefmt='fancy_grid')
      print(tabla)
      print(f'\nPolinomio: {self.generar_polionomio()}\n')