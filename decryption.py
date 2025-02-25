'''
 * Nombre: decryption.py
 * Descripción: Programa que desencripta un mensaje cifrado.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 21.02.2025
    - Finalizado el 24.02.2025
'''

import random

'''
String to Binary
'''
def stringToBinary(text):
    binary = ''

    for char in text:
        asciiVal = ord(char)
        binaryChar = ''
        temp = asciiVal
        
        if temp == 0:
            binaryChar = '0'
        
        while temp > 0:
            binaryChar = str(temp % 2) + binaryChar
            temp = temp // 2
            
        binaryChar = binaryChar.zfill(8)
        binary += binaryChar
    
    return binary

'''
XOR de los binarios
'''
def xorBinary(bin1, bin2):
    #Verificar que ambos binarios tengan la misma longitud
    maxLength = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(maxLength)  #Rellenar con ceros a la izquierda
    bin2 = bin2.zfill(maxLength)
    
    #Aplicar XOR
    xorResult = ''
    for b1, b2 in zip(bin1, bin2):
        xorResult += '1' if b1 != b2 else '0'

    return xorResult

'''
Keystream Generator
'''
def keystreamGenerator(messageLen, seed):
    #Inicializa el generador con la semilla proporcionada
    random.seed(seed)
    
    #Genera caracteres aleatorios para formar un string de la misma longitud
    keystream = ''
    for _ in range(messageLen):
        #Genera un carácter aleatorio del conjunto de dígitos hexadecimales
        hexChar = format(random.randint(0, 15), 'x')  #'x' formatea como un solo dígito hexadecimal
        keystream += hexChar
    
    return keystream

'''
Binary to String
'''
def binaryToString(binary):
    if len(binary) % 8 != 0:
        raise ValueError("La longitud de la cadena binaria debe ser múltiplo de 8")
    
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        decimalVal = 0
        for bit in byte:
            decimalVal = decimalVal * 2 + int(bit)
        
        character = chr(decimalVal)
        text += character
    
    return text

'''
Desencriptar mensaje
'''
def decryptMessage(text, keystream):
    bin1 = stringToBinary(text)
    bin2 = stringToBinary(keystream)

    xor = xorBinary(bin1, bin2)

    return binaryToString(xor)

'''
Función principal que maneja la interacción con el usuario.
'''
def main():
    while True:
        #Imprimir menú
        print("\n1. Desencriptar mensaje")
        print("2. Salir")
        choice = input("\nSeleccione una opción (1-2): ")
        
        #Salir
        if choice == "2":
            break
        
        #Validar opción
        if choice not in ["1"]:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
            continue
        
        #Obtener texto
        text = input("\nIngrese el texto a descifrar: ")
        keystream = input("Ingrese el keystream: ")
        
        #Validar texto
        if not text or not keystream:
            print("El texto o seed no puede estar vacío")
            continue
        
        #Cifrar
        if choice == "1":
            decryptedText = decryptMessage(text, keystream)

            print(f"\nTexto descifrado: {decryptedText}")

if __name__ == "__main__":
    main()