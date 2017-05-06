#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse, time, os

from argparse import RawTextHelpFormatter

from Utilidad import Utilidad
from ControladorPrincipal import ControladorATexto, ControladorABin

parser = argparse.ArgumentParser(description="""Contextualización:
	CriptografiaClasica es una aplicación de escritorio (standalone) que permite cifrar tanto archivos de texto como binarios,
	usando métodos de criptografía clásica.""", formatter_class=RawTextHelpFormatter)
parser._positionals.title = "Argumentos obligatorios"
parser._optionals.title = "Argumentos opcionales"

def main():
	argv = inicializarBanderas()
	print("Procesando...")
	t_ini = time.time()
	if argv.alg == 'ts':
		controlarTSD(argv)
		t_fin = time.time()
		t_total = t_fin - t_ini
		print("\nTiempo total: %.3f" % t_total+" seg.")
	elif argv.alg == 'tg':
		controlarTG(argv)
		t_fin = time.time()
		t_total = t_fin - t_ini
		print("\nTiempo total: %.3f" % t_total+" seg.")
	elif argv.alg == 'tse':
		controlarTS(argv)
		t_fin = time.time()
		t_total = t_fin - t_ini
		print("\nTiempo total: %.3f" % t_total+" seg.")
	elif argv.alg == 'po':
		controlarPO(argv)
		t_fin = time.time()
		t_total = t_fin - t_ini
		print("\nTiempo total: %.3f" % t_total+" seg.")
	elif argv.alg == 'pl':
		controlarPL(argv)	
		t_fin = time.time()
		t_total = t_fin - t_ini
		print("\nTiempo total: %.3f" % t_total+" seg.")
	elif argv.alg == 'ce':
		controlarCE(argv)
		t_fin = time.time()
		t_total = t_fin - t_ini
		print("\nTiempo total: %.3f" % t_total+" seg.")

def inicializarBanderas():
	parser.add_argument('-m', '--modo', help="""cifrar o descifrar el archivo""", choices=['cif','desc'])
	parser.add_argument('-alg', help="""Algoritmo que se va a utilizar
	ALGORITMO
	ts     Transposición SIMPLE (clave = cantidad que desea volver correr el algoritmo ej:0, 1, 2, ...)
	tg     transposición por GRUPOS (clave = archivoTexto con la secuencia separado por "," ej:1,3,2,4)
	tse     Transposición por SERIES (clave = archivoTexto con las series separado por un salto de línea ej: 1,2,3
		\t\t\t\t\t\t\t\t\t\t\t\t4,5,6)
	po     Sustitución monoalfabética POLYBIOS
	pl     Sustitución monoalfabética poligrámica digrámica PLAYFAR (clave = archivoTexto con la cadena clave ej:VWXY)
	ce     Sustitución monoalfabética por desplazamieto CESAR (clave = según el desplazamiento ej: 0,1,2,3,...)""", choices=['ts', 'tg', 'tse', 'po', 'pl', 'ce'])
	parser.add_argument('-kc', '--kcifrar', help='Clave necesaria para cifrar de cada algoritmo (excepto POLYBIOS)', metavar="CLAVE_CIF", default=0)
	parser.add_argument('-it', '--itxt', help='Archivo de entrada con extension txt', metavar="TXT")
	parser.add_argument('-ib', '--ibin', help='Archivo de entrada con extension diferente a txt', metavar="BIN")
	parser.add_argument('-alp', '--alphabet', help='Alfabeto con el cual se desea cifrar(inglés - español)', choices=['en_min', 'es_min', 'es_may', 'en_may'], default= "es_may")
	parser.add_argument("-kd", "--kdescifrar", help="Clave necesaria para descifrar de cada algoritmo (excepto POLYBIOS)", metavar="KDESC")

	args = parser.parse_args()
	return args

def controlarTSD(argv):
	# -alg ts -m cif|desc -kc 0 -it|ib ...
	itxt, ibin = validarEntradas(argv)

	modo = obtenerModo(argv)
	if itxt != None:
		if modo == "cif":
			cat = ControladorATexto()
			n = obtenerClaveCif(argv)
			validarTamanio(obtenerTipoEntrada(argv)[0])
			cat.cifrarcTSD(int(n), obtenerTipoEntrada(argv)[0])
		if modo == "desc":
			cat = ControladorATexto()
			n = obtenerClaveDesc(argv)
			cat.descifrarcTSD(obtenerTipoEntrada(argv)[0], n)
	if ibin != None:
		if modo == "cif":
			cab = ControladorABin()
			n = obtenerClaveCif(argv)
			validarTamanio(obtenerTipoEntrada(argv)[1])
			cab.cifrarcTSD(int(n), obtenerTipoEntrada(argv)[1])
		if modo == "desc":
			cab = ControladorABin()
			n = obtenerClaveDesc(argv)
			cab.descifrarcTSD(obtenerTipoEntrada(argv)[1], n)

#Problema con varias líneas con diferentes tamaños
def controlarTG(argv):
	# -alg tg -m cif|desc -kc ... -it ...
	itxt, ibin = validarEntradas(argv)

	modo = obtenerModo(argv)
	if itxt != None:
		if modo == "cif":
			cat = ControladorATexto()
			n = obtenerClaveCif(argv)
			n = establecerGrupos(n)
			validarTamanio(obtenerTipoEntrada(argv)[0])
			cat.cifrarcTG(n, obtenerTipoEntrada(argv)[0])
		if modo == "desc":
			cat = ControladorATexto()
			n = obtenerClaveDesc(argv)
			n = establecerGrupos(n)
			cat.descifrarcTG(obtenerTipoEntrada(argv)[0], n)
	if ibin != None:
		if modo == "cif":
			cab = ControladorABin()
			n = obtenerClaveCif(argv)
			n = establecerGrupos(n)
			validarTamanio(obtenerTipoEntrada(argv)[1])
			cab.cifrarcTG(n, obtenerTipoEntrada(argv)[1])
		if modo == "desc":
			cab = ControladorABin()
			n = obtenerClaveDesc(argv)
			n = establecerGrupos(n)
			cab.descifrarcTG(obtenerTipoEntrada(argv)[1], n)

#Sin archivos BIN
def controlarTS(argv):
	# -alg tse -m cif|desc -kc "series" -it "archivo"
	itxt, ibin = validarEntradas(argv)

	modo = obtenerModo(argv)
	if itxt != None:
		if modo == "cif":
			cat = ControladorATexto()
			n = obtenerClaveCif(argv)
			n = establecerSeries(n)
			validarTamanio(obtenerTipoEntrada(argv)[0])
			cat.cifrarcTS(n, obtenerTipoEntrada(argv)[0])
		if modo == "desc":
			cab = ControladorATexto()
			n = obtenerClaveDesc(argv)
			cab.descifrarcTS(obtenerTipoEntrada(argv)[0], n)

def controlarPO(argv):
	itxt, ibin = validarEntradas(argv)
	alfabeto = obtenerAlfabeto(argv)
	modo = obtenerModo(argv)
	if itxt != None:
		if modo == "cif":
			cat = ControladorATexto()
			cat.definirAlfabetoPolybios(alfabeto)
			validarTamanio(obtenerTipoEntrada(argv)[0])
			cat.cifrarPB(obtenerTipoEntrada(argv)[0], 0, '')
		if modo == "desc":
			cab = ControladorATexto()
			cab.definirAlfabetoPolybios(alfabeto)
			cab.descifrarPB(obtenerTipoEntrada(argv)[0], 0, '')

def controlarPL(argv):
	itxt, ibin = validarEntradas(argv)
	alfabeto = obtenerAlfabeto(argv)
	modo = obtenerModo(argv)
	if itxt != None:
		if modo == "cif":
			cat = ControladorATexto()
			cat.definirAlfabetoPlayfair(alfabeto)
			n = obtenerClaveCif(argv)
			validarTamanio(obtenerTipoEntrada(argv)[0])
			cat.cifrarPF(obtenerTipoEntrada(argv)[0], 0, n)
		if modo == "desc":
			cab = ControladorATexto()
			cab.definirAlfabetoPlayfair(alfabeto)
			n = obtenerClaveCif(argv)
			cab.descifrarPF(obtenerTipoEntrada(argv)[0], 0, n)

def controlarCE(argv):
	itxt, ibin = validarEntradas(argv)
	alfabeto = obtenerAlfabeto(argv)
	modo = obtenerModo(argv)
	if itxt != None:
		if modo == "cif":
			cat = ControladorATexto()
			n = obtenerClaveCif(argv)
			cat.definirAlfabetoCesar(alfabeto)
			validarTamanio(obtenerTipoEntrada(argv)[0])
			cat.cifrarCS(obtenerTipoEntrada(argv)[0], 0, int(n))
		if modo == "desc":
			cab = ControladorATexto()
			cab.definirAlfabetoCesar(alfabeto)
			n = obtenerClaveDesc(argv)
			cab.descifrarCS(obtenerTipoEntrada(argv)[0], 0, int(n))

def validarEntradas(argv):
	itxt, ibin = obtenerTipoEntrada(argv)
	if itxt == None and ibin == None:
		print("Debe seleccionar el tipo de entrada -it | -ib")
		exit(1)
	return itxt, ibin

def obtenerModo(argv):
	return argv.modo

def obtenerAlfabeto(argv):
	return argv.alphabet

def obtenerTipoEntrada(argv):
	return argv.itxt, argv.ibin

def obtenerClaveCif(argv):
	return argv.kcifrar

def obtenerClaveDesc(argv):
	return argv.kdescifrar

def establecerGrupos(archivo):
	utilidad = Utilidad()
	grupos1 = utilidad.leerArchivo(archivo, "r").split("\n")
	grupos2 = grupos1[0].split(",")
	grupos2 = ''.join(grupos2)
	return int(grupos2)


def establecerSeries(archivo):
	utilidad = Utilidad()
	series = utilidad.leerArchivo(archivo, "r").split("\n")
	serie = list()
	funcion = list()
	for i in series:
		funcion = i.split(",")
		serie.append(funcion)
	serie.pop()
	return serie

def validarTamanio(archivo):
	bytes =  int(os.stat(archivo).st_size)
	mb = bytesto(bytes, "m")
	if mb > 5:
		print("Sólamente se puede cifrar archivos menores a 5MB")
		exit(1)

#Fragmento tomado de: https://gist.github.com/shawnbutts/3906915
def bytesto(bytes, to, bsize=1024):
	a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
	r = float(bytes)
	for i in range(a[to]):
		r = r / bsize
	return r

if __name__ == '__main__':
	if not os.path.exists("./salida/"):
		os.makedirs("./salida/")
	main()