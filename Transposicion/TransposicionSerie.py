#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys

class TransposicionSerie(object):
	def __init__(self, series, cadena=None):
		self.cadena = cadena
		self.series = series
		self.textoClaro = ""
		self.textoCifrado = ""

	def cifrar(self):
		textoCifrado = ""
		linea_a_cifrar = ""
		saltosLinea = len(self.cadena)-1
		numFunciones = len(self.series)
		i = 0
		j = 0

		for linea in self.cadena:
			while i < numFunciones:
				linea_a_cifrar += self.aplicarSeries(linea, i, len(self.series[i]))
				i += 1
			if j < saltosLinea:
				textoCifrado += linea_a_cifrar + "\n"
				j += 1
			else:
				textoCifrado += linea_a_cifrar

			linea_a_cifrar = ""
			i = 0

		print(textoCifrado)

	def descifrar(self):
		#textoDescifrado = ""
		pass

	def aplicarSeries(self, linea, i, tamanioFuncion):
		lineaNueva = ""
		j = 0
		while j < tamanioFuncion:
			lineaNueva += linea[ int(self.series[i][j])-1 ]
			j += 1
		return lineaNueva


series1 = sys.argv[1].split(",")
series2 = sys.argv[2].split(",")
series3 = sys.argv[3].split(",")

serie = list()
serie.append(series1)
serie.append(series2)
serie.append(series3)

print(serie)
ts = TransposicionSerie(serie, "Holamundo\nVVosotros".split("\n"))
ts.cifrar()