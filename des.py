'''
 * Nombre: des.py
 * Descripción: Programa que implementa cifrado mediante DES.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 06.03.2025
    - Finalizado el 06.03.2025
'''

from Crypto.Cipher import DES
import os
import binascii

def generateKey():
    key = os.urandom(8) #key de 64 bits (8 bytes)

    return key

def manualPadding(data):
    # Asegurarse de que data es bytes, no string
    if isinstance(data, str):
        data = data.encode('utf-8')
        
    #Bloque DES en bytes (8)
    blockSize = 8
    
    #Calcular la cantidad de bytes de relleno necesarios
    paddingLen = blockSize - (len(data) % blockSize)
    
    if paddingLen == 0:
        paddingLen = blockSize
    
    #Aplicar padding
    padding = bytes([paddingLen] * paddingLen)
    
    #Añadir el relleno a los datos
    return data + padding

def deletePadding(data):
    #Ultimo byte indica cuantos bytes de relleno hay
    paddingLen = data[-1]
    
    #El relleno es valido
    if paddingLen > 8:
        raise ValueError("Relleno inválido: longitud de relleno mayor que el tamaño del bloque")
    
    #Verificar que todos los bytes de relleno tienen el valor correcto
    for i in range(1, paddingLen + 1):
        if data[-i] != paddingLen:
            raise ValueError("Relleno inválido: valores de relleno incorrectos")
    
    #Eliminar los bytes de relleno
    return data[:-paddingLen]

def encryptDES(plaintext, key):
    #Aplicar padding
    paddedText = manualPadding(plaintext)
    
    #Crear objeto de cifrado DES en modo ECB
    cipher = DES.new(key, DES.MODE_ECB)
    
    #Cifrar los datos
    cipherText = cipher.encrypt(paddedText)
    
    #Convertir a representación hexadecimal para facilitar su manejo
    cipherTextHex = binascii.hexlify(cipherText).decode('ascii')
    keyHex = binascii.hexlify(key).decode('ascii')
    
    return cipherTextHex, keyHex

def decryptDES(ciphertext, key):
    #Convertir de representación hexadecimal a bytes
    ciphertext = binascii.unhexlify(ciphertext)
    key = binascii.unhexlify(key)

    #Crear objeto de descifrado DES en modo ECB
    cipher = DES.new(key, DES.MODE_ECB)
    
    #Descifrar los datos
    decryptedText = cipher.decrypt(ciphertext)
    
    # Eliminar el relleno
    unpaddedText = deletePadding(decryptedText)
    
    #Convertir de bytes a cadena
    result = unpaddedText.decode('utf-8')
    
    return result

# Ejemplo de uso
def main():
    while True:
        #Imprimir menú
        print("\n1. Desencriptar mensaje")
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
        
        #Obtener texto
        text = input("\nIngrese el texto a cifrar/descifrar: ")
        
        #Validar texto
        if not text:
            print("El texto no puede estar vacío.")
            continue
        
        #Cifrar
        if choice == "1":
            genKey = generateKey()
            encryptedText, key = encryptDES(text, genKey)

            print(f"\nTexto cifrado: {encryptedText}")
            print(f"Llave generada: {key}")
            
        #Descifrar
        elif choice == "2":
            key = input("Ingrese la llave: ")
            #Validar texto
            if not key:
                print("La llave no puede estar vacía.")
                continue

            decryptedText = decryptDES(text, key)
            print(f"\nTexto descifrado: {decryptedText}")

if __name__ == "__main__":
    main()