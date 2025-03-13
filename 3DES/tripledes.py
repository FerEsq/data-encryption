'''
 * Nombre: tripledes.py
 * Descripción: Programa que implementa cifrado mediante 3DES en modo CBC.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 12.03.2025
    - Finalizado el 12.03.2025
'''

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii
import os

def generateKey():
    #Generar llave aleatoria de 24 bytes (192 bits)
    key = DES3.adjust_key_parity(get_random_bytes(24)) #La key debe tener paridad impar en cada byte para 3DES
    return key

def generateIV():
    #El tamaño del bloque para 3DES es de 8 bytes
    return get_random_bytes(8)

def encrypt3des(plaintext, key, iv):    
    #Convertir el texto plano a bytes si es una cadena
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    #Crear objeto de cifrado 3DES en modo CBC
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    
    #Padding (el tamaño del bloque para 3DES es de 8 bytes)
    paddedData = pad(plaintext, DES3.block_size)
    
    #Cifrar los datos
    encryptedText = cipher.encrypt(paddedData)
    
    #Convertir a representación hexadecimal para facilitar manejo
    encryptedHex = binascii.hexlify(encryptedText).decode('ascii')
    keyHex = binascii.hexlify(key).decode('ascii')
    ivHex = binascii.hexlify(iv).decode('ascii')
    
    return encryptedHex, keyHex, ivHex

def decrypt3des(ciphertextHex, keyHex, ivHex):
    try:
        #Convertir de representación hexadecimal a bytes
        ciphertext = binascii.unhexlify(ciphertextHex)
        key = binascii.unhexlify(keyHex)
        iv = binascii.unhexlify(ivHex)
        
        #Crear objeto de descifrado 3DES en modo CBC
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        
        # Descifrar los datos
        padded_plaintext = cipher.decrypt(ciphertext)
        
        #Eliminar padding
        try:
            plaintext = unpad(padded_plaintext, DES3.block_size)
        except ValueError as e:
            print(f"Advertencia: Error al eliminar el padding: {e}")
            print("Intentando recuperar el texto sin eliminar el padding...")
            plaintext = padded_plaintext
        
        # Intentar decodificar con UTF-8
        try:
            decryptedText = plaintext.decode('utf-8')
        except UnicodeDecodeError:
            # Si falla la decodificación, usar 'replace' para sustituir caracteres inválidos
            decryptedText = plaintext.decode('utf-8', errors='replace')
        
        return decryptedText
    except binascii.Error as e:
        print(f"Error al procesar datos hexadecimales: {e}")
        return None
    except Exception as e:
        print(f"Error al descifrar: {e}")
        return None

def readFile(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{filePath}' no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def writeFile(text, filePath):
    try:
        with open(filePath, 'w', encoding='utf-8') as archivo:
            archivo.write(text)
        return True
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
        return False

def main():
    while True:
        #Imprimir menú
        print("\n1. Encriptar mensaje")
        print("2. Desencriptar mensaje")
        print("3. Salir")
        choice = input("\nSeleccione una opción (1-3): ")
        
        #Salir
        if choice == "3":
            break
        
        #Validar opción
        if choice not in ["1", "2"]:
            print("Opción no válida.")
            continue

        #Cifrar
        if choice == "1":
            #Leer el archivo
            text = readFile("3DES\message.txt")
            if text is None:
                continue
            
            #Generar llave y IV
            genKey = generateKey()
            iv = generateIV()
            
            #Cifrar el texto
            encryptedText, keyHex, ivHex = encrypt3des(text, genKey, iv)
            
            #Guardar el texto cifrado
            outputPath = "3DES\decrypted.txt"
            
            if writeFile(encryptedText, outputPath):
                print(f"\nTexto cifrado guardado en '{outputPath}'")
                
                #Mostrar la llave y el IV
                print(f"\nLlave (KEY): {keyHex}")
                print(f"Vector de inicialización (IV): {ivHex}")
            
        #Descifrar
        elif choice == "2":
            #Pedir la ruta del archivo cifrado
            inputFile = "3DES\decrypted.txt"
            
            #Leer el archivo cifrado
            encryptedText = readFile(inputFile)
            if encryptedText is None:
                continue
            
            #Pedir la llave y el IV manualmente
            keyHex = input("Ingrese la llave (KEY): ")
            ivHex = input("Ingrese el vector de inicialización (IV): ")
            
            #Validar entradas
            if not keyHex or not ivHex:
                print("La llave y el IV no pueden estar vacíos.")
                continue
            
            #Descifrar
            decryptedText = decrypt3des(encryptedText, keyHex, ivHex)
            if decryptedText:
                #Guardar el resultado
                outputPath = "3DES\decrypted.txt"
                
                if writeFile(decryptedText, outputPath):
                    print(f"\nTexto descifrado guardado en '{outputPath}': \n{decryptedText}")
                    
            else:
                print("No se pudo descifrar el texto.")

if __name__ == "__main__":
    main()