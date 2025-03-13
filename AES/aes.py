'''
 * Nombre: aes.py
 * Descripción: Programa que implementa cifrado y descifrado AES con CBC Y ECB.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 12.03.2025
    - Finalizado el 13.03.2025
'''

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import os
from PIL import Image
import numpy as np

#Rutas de archivos
imagePath = "AES/image.png" 
cbcPath = "AES/cbc.png"  
ecbPath = "AES/ecb.png"  

def generateKey():
    return get_random_bytes(32)  #256 bits = 32 bytes

def generateIV():
    return get_random_bytes(AES.block_size)  #16 bytes para AES

def encryptCBC(image_path, output_path, key):
    #Cargar imagen
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    
    #Convertir imagen a bytes
    imgBytes = np.array(img).tobytes()
    
    #Aplicar padding
    paddedData = pad(imgBytes, AES.block_size)
    
    #Generar IV y cifrar con CBC
    iv = generateIV()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encryptedBytes = cipher.encrypt(paddedData)
    
    #Convertir bytes cifrados de vuelta a una imagen
    encryptedArray = np.frombuffer(encryptedBytes, dtype=np.uint8)
    try:
        #Intentar mantener las dimensiones originales
        encryptedArray = encryptedArray[:width*height*3].reshape((height, width, 3))
    except ValueError:
        #Si hay un problema con las dimensiones, ajustar la forma
        totalPixels = len(encryptedBytes) // 3
        newHeight = int(np.sqrt(totalPixels))
        newWidth = totalPixels // newHeight
        encryptedArray = encryptedArray[:newHeight*newWidth*3].reshape((newHeight, newWidth, 3))
    
    #Guardar imagen cifrada
    Image.fromarray(encryptedArray).save(output_path)
    return True

def encryptECB(image_path, output_path, key):
    #Cargar imagen
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    
    #Convertir imagen a bytes
    imgBytes = np.array(img).tobytes()
    
    #Aplicar padding
    paddedData = pad(imgBytes, AES.block_size)
    
    #Cifrar con ECB
    cipher = AES.new(key, AES.MODE_ECB)
    encryptedBytes = cipher.encrypt(paddedData)
    
    #Convertir bytes cifrados de vuelta a una imagen
    encryptedArray = np.frombuffer(encryptedBytes, dtype=np.uint8)
    try:
        #Intentar mantener las dimensiones originales
        encryptedArray = encryptedArray[:width*height*3].reshape((height, width, 3))
    except ValueError:
        #Si hay un problema con las dimensiones, ajustar la forma
        totalPpixels = len(encryptedBytes) // 3
        newHeight = int(np.sqrt(totalPpixels))
        newWidth = totalPpixels // newHeight
        encryptedArray = encryptedArray[:newHeight*newWidth*3].reshape((newHeight, newWidth, 3))
    
    #Guardar imagen cifrada
    Image.fromarray(encryptedArray).save(output_path)
    return True

def main():
    while True:
        #Imprimir menú
        print("\n1. Cifrar imagen con AES-CBC")
        print("2. Cifrar imagen con AES-ECB")
        print("3. Salir")
        choice = input("\nSeleccione una opción (1-3): ")
        
        #Salir
        if choice == "3":
            break
        
        #Validar opción
        if choice not in ["1", "2"]:
            print("Opción no válida.")
            continue

        # Verificar que la imagen de entrada existe
        if not os.path.exists(imagePath):
            print(f"Error: La imagen '{imagePath}' no existe.")
            return

        #Generar llave
        key = generateKey()
        
        #Cifrar con CB
        if choice == "1":
            encryptCBC(imagePath, cbcPath, key)
            print(f"Imagen cifrada con CBC guardada en {cbcPath}")


        #Cifrar con ECB
        elif choice == "2":
            encryptECB(imagePath, ecbPath, key)
            print(f"Imagen cifrada con ECB guardada en {ecbPath}")

if __name__ == "__main__":
    main()