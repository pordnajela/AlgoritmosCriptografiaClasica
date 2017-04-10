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
		self.saltosLinea = {"GNU/UNIX": "\n","WINDOWS":"\r\n"}

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

		charset1 = subprocess.Popen("file -bi "+archivo+"| awk '{print $2}'",shell=True, stdout=subprocess.PIPE)
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
		so = ""
		with open(archivo, "rb") as archOrig:
			saltoLinea = archOrig.read().split(b"\n")
		archOrig.close()
		if saltoLinea[0][-1] == 13:
			so = "WINDOWS"
		else:
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

	"""
	Permite saber si un archivo debe tratarse como un TXT (texto plano) o no según su codificación.

	Parámetros:
	codificación: 
	"""
	def esTxt(self, codificacion):
		return codificacion in self.formatosTxt

	"""
	"""
	def crearArchivoCifrado(self,archivo,texto):
		archivo = open(self.dirSalida+archivo+".CIF","w")
		archivo.write(texto)
		archivo.close()

	"""
	"""
	def crearArchivoMetadatos(self,nombre,extension,codificacion,so):
		archivo = open(self.dirSalida+nombre+".mdt","w")
		archivo.write(nombre+"\n")
		archivo.write(extension+"\n")
		archivo.write(codificacion+"\n")
		archivo.write(so)
		archivo.close()

	def comprobarHash(self,archivoOrigen, archivoDescifrado):
		pass

'''
def convertirBase64(textoUTF8):
	cadenaBase64 = base64.b64encode(textoUTF8)
	return cadenaBase64, cadenaBase64.decode("utf-8")
'''