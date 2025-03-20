'''
 * Nombre: decryption.py
 * Descripción: Script de descifrado de archivos de texto en un directorio usando AES.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 18.03.2025
    - Finalizado el 20.03.2025
'''

#!/usr/bin/env python3
"""
Script para descifrar archivos previamente cifrados con AES usando la librería pycryptodome.
Este script recorre un directorio y descifra todos los archivos .enc usando la clave guardada en key.txt
"""

import os
import sys
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decryptFile(filepath, key):
    #Verificar que el archivo es un archivo cifrado
    if not filepath.endswith('.enc'):
        print(f"Advertencia: {filepath} no parece ser un archivo cifrado (.enc). Omitiendo.")
        return None
    
    #Leer el archivo cifrado
    with open(filepath, 'rb') as f:
        #Los primeros 16 bytes son el IV
        iv = f.read(16)
        #El resto es el ciphertext
        ciphertext = f.read()
    
    #Crear el objeto de descifrado AES
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    try:
        #Descifrar y quitar el padding
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        
        #Nombre del archivo descifrado (quitar .enc)
        decryptedFilepath = filepath[:-4] + '.dec'
        
        #Guardar el archivo descifrado
        with open(decryptedFilepath, 'wb') as f:
            f.write(plaintext)
        
        print(f"Archivo descifrado: {decryptedFilepath}")
        
        return decryptedFilepath
    
    except Exception as e:
        print(f"Error al descifrar {filepath}: {e}")
        return None

def processDirectory(dirpath, key):
    #Recorrer el directorio buscando archivos .enc
    decryptedFiles = []
    for root, _, files in os.walk(dirpath):
        for file in files:
            if file.endswith('.enc'):
                file_path = os.path.join(root, file)
                decrypted_file = decryptFile(file_path, key)
                if decrypted_file:
                    decryptedFiles.append(decrypted_file)
    
    return decryptedFiles

def main():    
    directory_path = input("Ingrese la ruta del directorio a descifrar: ") #Part4/data
    
    #Verificar que el directorio existe
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' no es un directorio válido.")
        sys.exit(1)
    
    #Buscar el archivo key.txt
    keyFile = os.path.join(directory_path, 'key.txt')
    if not os.path.isfile(keyFile):
        print(f"Error: No se encontró el archivo 'key.txt' en el directorio '{directory_path}'.")
        print("Este archivo es necesario para descifrar correctamente los archivos.")
        sys.exit(1)
    
    #Leer la clave del archivo
    with open(keyFile, 'rb') as f:
        encoded_key = f.read()
    
    #Decodificar la clave de base64
    key = base64.b64decode(encoded_key)
    
    #Procesar el directorio
    decryptedFiles = processDirectory(directory_path, key)
    
    #Mostrar resumen
    print(f"\nTotal de archivos descifrados: {len(decryptedFiles)}")
    
    if len(decryptedFiles) == 0:
        print("\nNo se encontraron archivos para descifrar o hubo errores en el proceso.")
        print("Asegúrese de que la clave en key.txt sea correcta y que existan archivos .enc en el directorio.")

if __name__ == "__main__":
    main()