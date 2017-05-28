#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from Plantilla import Template
from Transposicion.TransposicionSimple import TransposicionSimple
from Transposicion.TransposicionGrupo import TransposicionGrupo
from Transposicion.TransposicionSerie import TransposicionSerie

class ControladorTransposicionSD(Template):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self, n=None, archivoOriginal=None):
		Template.__init__(self)
		self.tSimple = TransposicionSimple()
		self.n = n
		self.archivoOriginal = archivoOriginal
	
	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
		except IndexError:
			pass

		self.tSimple.cadena = cadena
		self.tSimple.cifrar()

		for x in range(0, self.n):
			self.tSimple.cadena = self.tSimple.textoCifrado.split("\n")
			self.tSimple.cifrar()

		return self.tSimple.textoCifrado
	
	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			clave = argumentos[1]
		except IndexError:
			pass

		self.n = int(clave)
		self.tSimple.cadena = cadena
		self.tSimple.descifrar()
		
		for x in range(0, self.n):
			self.tSimple.cadena = self.tSimple.textoClaro.split("\n")
			self.tSimple.descifrar()

		return self.tSimple.textoClaro

	#------------------------------------------------------------------------------------------------

class ControladorTransposicionGrupo(Template):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self, clave=None, archivoOriginal=None):
		Template.__init__(self)
		self.tGrupo = TransposicionGrupo(None, clave)
		self.archivoOriginal = archivoOriginal

	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
		except IndexError:
			pass
		'''
		nombre = ControladorTransposicionTemplate.obtenerArchivoMetadatos(self,self.archivoOriginal)[0]
		self.utilidad.crearArchivo(nombre+".mtd", str(self.tGrupo.clave)+"\n", "a")
		'''
		self.tGrupo.cadena = cadena
		self.tGrupo.cifrar()
		return self.tGrupo.textoCifrado

	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			clave = argumentos[1]
		except IndexError:
			pass

		self.tGrupo.clave = int(clave)
		self.tGrupo.cadena = cadena
		self.tGrupo.descifrar()

		cadenaDescifradaRelleno =self.tGrupo.textoClaro.split("\n")
		cadenaSinRelleno = self.tGrupo.eliminarRelleno(cadenaDescifradaRelleno)
		self.tGrupo.textoClaro = cadenaSinRelleno
		
		return self.tGrupo.textoClaro

	#------------------------------------------------------------------------------------------------

class ControladorTransposicionSerie(Template):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self, funciones=None, archivoOriginal=None):
		Template.__init__(self)
		'''Funciones es una lista, donde cada posición es una lista de números que 
		corresponde a una función en particular. Ej: [ [1,2,3,5,7], [4,6,8], [9] ]'''
		self.tSerie = TransposicionSerie(funciones)
		self.archivoOriginal = archivoOriginal
	
	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
		except IndexError:
			pass

		self.tSerie.cadena = cadena
		self.tSerie.cifrar()
		
		return self.tSerie.textoCifrado

	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			clave = argumentos[1]
		except IndexError:
			pass

		self.tSerie.series = clave
		self.tSerie.cadena = cadena
		self.tSerie.descifrar()
		return self.tSerie.textoClaro