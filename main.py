#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import os
from time import time

from Utilidad import Utilidad
from ControladorPrincipal import ControladorATexto, ControladorABin

def main():
	pass

def establecerSeries(archivo):
	utilidad = Utilidad()
	series = utilidad.leerArchivo(archivo, "r").split("\n")
	serie = list()
	funcion = list()
	for i in series:
		funcion = i.split(",")
		serie.append(funcion)
	return serie

if __name__ == '__main__':
	main()