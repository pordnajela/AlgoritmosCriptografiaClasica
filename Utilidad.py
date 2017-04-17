#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import subprocess
import os
import base64

class Utilidad(object):
	def __init__(self):
		self.formatosTxt = ["ISO-8859-1","UTF-8"]
		self.dirSalida = "./salida/"

	"""
	Obtiene la codificación actual del archivo seleccionado, su nombre y extension.
	Se ejecuta el comando file -bi [archivo] | awk '{print $2}' para obtener la codificación como cadena

	Parámetros:
	archivo: Archivo que debe existir en el disco duro para obtener su respectiva cdificación.
	"""
	def obtenerMetadatos(self, archivo):
		esArchivo = os.path.isfile(archivo)

		if esArchivo:
			existe = os.path.exists(archivo)
			if existe == False:
				print("El archivo no existe")
				return 1
		else:
			print("El argumento debe ser un archivo, no una carpeta")
			return 1

		charset1 = subprocess.Popen("file -bi "+archivo+" | awk '{print $2}'",shell=True, stdout=subprocess.PIPE)
		codificacion,err = charset1.communicate()

		if err != None:
			print(err)
			return 1
		else:
			codificacion = codificacion.decode("utf-8")
			codificacion = codificacion.split("=")[1].strip("\n")

		#Obtener nombre y extension
		direccion, extension = os.path.splitext(archivo)
		nombre = direccion.split("/")[-1]

		#Obtener sistema operativo según su Línea Nueva
		so = None
		with open(archivo, "rb") as archOrig:
			saltoLinea = archOrig.read().split(b"\n")
		archOrig.close()
		if saltoLinea[0][-1] == 13:
			so = "WINDOWS"
		else:
			if self.esTxt(codificacion):
				so = "GNU/UNIX"

		return nombre, extension, codificacion.upper(), so

	"""
	Permite cambiar de codificación con el comando iconv, la cual tiene la siguiente sintaxis
	$ iconv -f [codOrigen] -t [codDestino] [archivoOrigen] > [archivoDestino]

	Parámetros:
	codOrigen: Codificación original del archivo tratar.
	codDestino: Codificación a la que se desea convertir.
	archivoOrigen: Archivo el cual contiene codOrigen.
	archivoDestino: Archivo que contiene la información de archivoOrigen pero en la codificación deseada.
	"""
	def resolverCodificacion(self, codOrigen, codDestino, archivoOrigen, archivoDestino):
		comando = "iconv -f "+codOrigen+" -t "+codDestino+" "+archivoOrigen+" > "+self.dirSalida+archivoDestino
		charset1 = subprocess.Popen(comando,shell=True, stdout=subprocess.PIPE)
		charset1.wait()

	'''
	Debido a que los archivos creados en WINDOWS tienen salto de líne CR (Carriage Return) y UNIX LF
	este método permite corregir ese detalle.

	Parámetros:
	archivo: Archivo que se desea manipular
	Más información ver < man unix2dos >
	'''
	def resolverSaltoLinea(self, archivo):
		comando = "unix2dos -q "+archivo
		charset1 = subprocess.Popen(comando,shell=True, stdout=subprocess.PIPE)
		charset1.wait()		

	"""
	Permite saber si un archivo debe tratarse como un TXT (texto plano) o no según su codificación.

	Parámetros:
	codificación: Según la codificación se deduce si es TXT u otro tipo de archivo
	"""
	def esTxt(self, codificacion):
		return codificacion in self.formatosTxt

	"""
	Permite crear archivos çon cualquier información

	Parámetros:
	archivo: Nombre del archivo a crear.
	texto: Ínformación que se adjunta al archivo.
	"""
	def crearArchivo(self,archivo,texto, modo):
		with open(self.dirSalida+archivo, modo) as archivo:
			archivo.write(texto)
		archivo.close()

	"""
	Permite crear el archivo de metadatos correspondiente al archivo a procesar.

	Parámetros:
	nombre: Nombre del archivo de metadatos a crear.
	argumentos: Lista de datos que corresponden a los metadatos (es variable)
	"""
	def crearArchivoMetadatos(self, nombre, *argumentos):
		with open(self.dirSalida+nombre+".mtd" , "w") as archivo:
			for arg in list(argumentos):
				archivo.write(arg+"\n")
		archivo.close()

	#TO-DO
	def removerEspacios(self):
		pass

	def comprobarHash(self,archivoOrigen, archivoDescifrado):
		import hashlib
		md5sum1 = hashlib.md5()
		md5sum2 = hashlib.md5()
		md5sum1.update(self.leerArchivo(archivoOrigen,"rb"))
		md5sum2.update(self.leerArchivo(archivoDescifrado,"rb"))

		return True if md5sum1.hexdigest() == md5sum2.hexdigest() else False

	'''
	Permite leer un archivo en memoria

	Parámetros:
	arch: Nombre del archivo a leer
	modo: Tipo de lectura (rb , r , rU)
	'''
	def leerArchivo(self, arch, modo):
		with open(arch, modo) as archivo:
			dato = archivo.read()
		archivo.close()
		return dato

	'''
	Permite obtener la codificación en Base64 de un archivo

	Parámetros:
	archivo: Archivo que se desea obtener Base64
	'''
	def obtenerBase64(self, archivo):
		cadena = self.leerArchivo(archivo, "rb")
		cadenaCodificada = base64.b64encode(cadena)
		cadenaCodificada = cadenaCodificada.decode()
		return cadenaCodificada

	def cadena_a_Base64(self, texto):
		criptogramaB64 = texto.encode()
		criptogramaBin = base64.b64decode(criptogramaB64)
		return criptogramaBin
