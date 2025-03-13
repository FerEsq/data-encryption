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
from Crypto.Util.Padding import pad, unpad
import os
from PIL import Image
import numpy as np
import binascii

#Rutas de archivos
imagePath = "AES/image.png" 
cbcEncPath = "AES/cbcEncrypted.png"
cbcDecPath = "AES/cbcDecrypted.png"
ecbEncPath = "AES/ecbEncrypted.png"
ecbDecPath = "AES/ecbDecrypted.png"

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
    
    #Devolver IV para el descifrado
    return iv

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
        totalPixels = len(encryptedBytes) // 3
        newHeight = int(np.sqrt(totalPixels))
        newWidth = totalPixels // newHeight
        encryptedArray = encryptedArray[:newHeight*newWidth*3].reshape((newHeight, newWidth, 3))
    
    #Guardar imagen cifrada
    Image.fromarray(encryptedArray).save(output_path)
    return True

def decryptCBC(encrypted_path, output_path, key, iv):
    try:
        #Cargar imagen cifrada
        img = Image.open(encrypted_path).convert('RGB')
        
        #Convertir imagen a bytes
        encryptedBytes = np.array(img).tobytes()
        
        #Crear objeto de descifrado
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        #Descifrar los bytes
        decryptedPadded = cipher.decrypt(encryptedBytes)
        
        #Eliminar el padding
        try:
            decryptedBytes = unpad(decryptedPadded, AES.block_size)
        except ValueError:
            # Si hay problemas con el padding, continuar sin quitar padding
            decryptedBytes = decryptedPadded
        
        #Convertir bytes a imagen
        width, height = img.size
        decryptedArray = np.frombuffer(decryptedBytes, dtype=np.uint8)
        try:
            decryptedArray = decryptedArray[:width*height*3].reshape((height, width, 3))
        except ValueError:
            # Si hay problemas con las dimensiones, hacer un ajuste
            totalPixels = len(decryptedBytes) // 3
            newHeight = int(np.sqrt(totalPixels))
            newWidth = totalPixels // newHeight
            decryptedArray = decryptedArray[:newHeight*newWidth*3].reshape((newHeight, newWidth, 3))
        
        #Guardar imagen descifrada
        Image.fromarray(decryptedArray).save(output_path)
        return True
    except Exception as e:
        print(f"Error al descifrar con CBC: {e}")
        return False

def decryptECB(encrypted_path, output_path, key):
    try:
        #Cargar imagen cifrada
        img = Image.open(encrypted_path).convert('RGB')
        
        #Convertir imagen a bytes
        encryptedBytes = np.array(img).tobytes()
        
        #Crear objeto de descifrado
        cipher = AES.new(key, AES.MODE_ECB)
        
        #Descifrar los bytes
        decryptedPadded = cipher.decrypt(encryptedBytes)
        
        #Eliminar el padding
        try:
            decryptedBytes = unpad(decryptedPadded, AES.block_size)
        except ValueError:
            # Si hay problemas con el padding, continuar sin quitar padding
            decryptedBytes = decryptedPadded
        
        #Convertir bytes a imagen
        width, height = img.size
        decryptedArray = np.frombuffer(decryptedBytes, dtype=np.uint8)
        try:
            decryptedArray = decryptedArray[:width*height*3].reshape((height, width, 3))
        except ValueError:
            # Si hay problemas con las dimensiones, hacer un ajuste
            totalPixels = len(decryptedBytes) // 3
            newHeight = int(np.sqrt(totalPixels))
            newWidth = totalPixels // newHeight
            decryptedArray = decryptedArray[:newHeight*newWidth*3].reshape((newHeight, newWidth, 3))
        
        #Guardar imagen descifrada
        Image.fromarray(decryptedArray).save(output_path)
        return True
    except Exception as e:
        print(f"Error al descifrar con ECB: {e}")
        return False

def main():
    while True:
        #Imprimir menú
        print("\n1. Cifrar imagen con AES-CBC")
        print("2. Cifrar imagen con AES-ECB")
        print("3. Descifrar imagen con AES-CBC")
        print("4. Descifrar imagen con AES-ECB")
        print("5. Salir")
        choice = input("\nSeleccione una opción (1-5): ")
        
        #Salir
        if choice == "5":
            break
        
        #Validar opción
        if choice not in ["1", "2", "3", "4"]:
            print("Opción no válida.")
            continue

        # Opciones de cifrado
        if choice in ["1", "2"]:
            # Verificar que la imagen de entrada existe
            if not os.path.exists(imagePath):
                print(f"Error: La imagen '{imagePath}' no existe.")
                continue

            # Generar llave
            key = generateKey()
            keyHex = binascii.hexlify(key).decode('ascii')
            print(f"\nLlave generada: {keyHex}")
            
            #Cifrar con CBC
            if choice == "1":
                iv = encryptCBC(imagePath, cbcEncPath, key)
                ivHex = binascii.hexlify(iv).decode('ascii')
                print(f"Vector de inicialización (IV): {ivHex}")
                print(f"Imagen cifrada con CBC guardada en {cbcEncPath}")

            #Cifrar con ECB
            elif choice == "2":
                encryptECB(imagePath, ecbEncPath, key)
                print(f"\nImagen cifrada con ECB guardada en {ecbEncPath}")
        
        # Opciones de descifrado
        elif choice in ["3", "4"]:
            # Solicitar clave
            keyHex = input("\nIngrese la key: ")
            try:
                key = binascii.unhexlify(keyHex)
            except binascii.Error:
                print("Error: La clave no es un valor hexadecimal válido.")
                continue
                
            #Descifrar con CBC
            if choice == "3":
                # Verificar que la imagen cifrada existe
                if not os.path.exists(cbcEncPath):
                    print(f"Error: La imagen cifrada '{cbcEncPath}' no existe.")
                    continue
                    
                # Solicitar IV
                ivHex = input("Ingrese el vector de inicialización (IV): ")
                try:
                    iv = binascii.unhexlify(ivHex)
                except binascii.Error:
                    print("Error: El IV no es un valor hexadecimal válido.")
                    continue
                
                if decryptCBC(cbcEncPath, cbcDecPath, key, iv):
                    print(f"\nImagen descifrada con CBC guardada en {cbcDecPath}")
                
            # Descifrar con ECB
            elif choice == "4":
                # Verificar que la imagen cifrada existe
                if not os.path.exists(ecbEncPath):
                    print(f"Error: La imagen cifrada '{ecbEncPath}' no existe.")
                    continue
                    
                if decryptECB(ecbEncPath, ecbDecPath, key):
                    print(f"\nImagen descifrada con ECB guardada en {ecbDecPath}")

if __name__ == "__main__":
    main()