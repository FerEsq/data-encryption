'''
 * Nombre: encryption.py
 * Descripción: Script de cifrado de archivos de texto en un directorio usando AES.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 18.03.2025
    - Finalizado el 20.03.2025
'''

import os
import sys
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def encryptFile(filepath, key):
    #Generar IV random
    iv = get_random_bytes(16)
    
    #Objeto de cifrado AES
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    #Leer txt
    with open(filepath, 'rb') as f:
        plaintext = f.read()
    
    #Aplicar padding y cifrar
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    
    #Crear el archivo cifrado (.enc)
    encryptedFilepath = filepath + '.enc'
    
    #Guardar el IV y el ciphertext en el archivo cifrado
    with open(encryptedFilepath, 'wb') as f:
        f.write(iv)
        f.write(ciphertext)
    
    print(f"Archivo cifrado: {encryptedFilepath}")
    
    return encryptedFilepath

def processDirectory(dirpath, key):
    #Guardar la clave en un archivo como base64 para facilitar su lectura
    keyFile = os.path.join(dirpath, 'key.txt')
    with open(keyFile, 'wb') as f:
        f.write(base64.b64encode(key))
    
    print(f"Clave guardada en: {keyFile}")
    
    #Recorrer el directorio buscando archivos .txt
    encryptedFiles = []
    for root, _, files in os.walk(dirpath):
        for file in files:
            if file.endswith('.txt') and file != 'key.txt':  #Evitar cifrar la clave
                file_path = os.path.join(root, file)
                encrypted_file = encryptFile(file_path, key)
                encryptedFiles.append(encrypted_file)
    
    return encryptedFiles

def main():
    directory_path = input("Ingrese la ruta del directorio a cifrar: ") #Part4/data

    #Verificar que el directorio existe
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' no es un directorio válido.")
        sys.exit(1)
    
    #Generar una clave aleatoria de 32 bytes (256 bits) para AES-256
    key = get_random_bytes(32)
    
    #Procesar el directorio
    encryptedFiles = processDirectory(directory_path, key)
    
    #Mostrar resumen

if __name__ == "__main__":
    main()