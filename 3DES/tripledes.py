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
        
        #Eliminar pading
        plaintext = unpad(padded_plaintext, DES3.block_size)
        
        #Convertir de bytes a cadena
        decrytptedText = plaintext.decode('utf-8')
        
        return decrytptedText
    except binascii.Error as e:
        print(f"Error al procesar datos hexadecimales: {e}")
        return None
    except Exception as e:
        print(f"Error al descifrar: {e}")
        return None

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

        text = input("Ingrese el texto a cifrar/decifrar: ")

        #Validar texto
        if not text:
            print("El texto no puede estar vacío.")
            continue

        
        #Cifrar
        if choice == "1":
            genKey = generateKey()
            iv = generateIV()
            encryptedText, key, iv_hex = encrypt3des(text, genKey, iv)

            print(f"\nTexto cifrado: {encryptedText}")
            print(f"Llave generada: {key}")
            print(f"Vector de inicialización (IV): {iv_hex}")  # Mostrar también el IV
            
        #Descifrar
        elif choice == "2":
            key = input("Ingrese la llave: ")
            iv = input("Ingrese el vector de inicialización (IV): ")
            
            #Validar texto
            if not key or not iv:
                print("La llave y el IV no pueden estar vacíos.")
                continue

            decryptedText = decrypt3des(text, key, iv)
            if decryptedText:
                print(f"\nTexto descifrado: {decryptedText}")

if __name__ == "__main__":
    main()