#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import argparse

from Utilidad import Utilidad
from ControladorPrincipal import ControladorATexto, ControladorABin

argv = sys.argv

parser = argparse.ArgumentParser(description="""%(prog)s es una aplicacion para generar archivos de texto cifrados usando metodos de criptografica clasica""")
print(parser._positionals.title)

def main():
	inicializarBanderas()

def inicializarBanderas():
	parser.add_argument('algoritmo', help="""Algoritmo que se va a utilizar
	ALGORITMO
	-ts     Transposición SIMPLE
	-td     Transposición DOBLE
	-gr     transposición por GRUPOS
	-se     Transposición por SERIES
	-po     Sustitución monoalfabética POLYBIOS
	-pl     Sustitución monoalfabética poligrámica digrámica PLAYFAR
	-ce     Sustitución monoalfabética por desplazamieto CESAR
	-fr     Analisis por frecuencia
	-af     Sustitución monoalfabética cifrado AFIN
	-vi     Sustitución polialfabética VIGENER
	-ka     Metodo de KASISKI
	-ve     Sustitucion polialfabetica VERAM""", choices=['ts', 'td', 'gr', 'se', 'po', 'ce', 'fr', 'af', 'vi', 'ka', 've'])
	parser.add_argument('archivo', help='Nombre del archivo que se va a cifrar o descifrar')
	parser.add_argument('modo', help='cifrar o descifrar el archivo', choices=['c', 'd'])

	args = parser.parse_args()

if __name__ == '__main__':
	main()