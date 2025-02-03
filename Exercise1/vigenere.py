'''
 * Nombre: vigenere.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Creado el 03.02.2025
    - Finalizado el 03.02.2025
'''

alphabet = "abcdefghijklmnñopqrstuvwxyz"

'''
Funciones auxiliares
'''
def cleanPlainText(text):
    text = text.lower()
    cleanChars = []

    for char in text:
        #Verificar si el carácter es una letra
        if char.isalpha():
            cleanChars.append(char)
    
    cleanText = ''.join(cleanChars)
    
    return cleanText

def dinamicKeyGenerator(key, length):    
    #Si la longitud es 0, retornar string vacío
    if length == 0:
        return ""
    
    #Calcular cuántas veces necesitamos repetir la key completa
    repeat = length // len(key)
    #Calcular cuántos caracteres adicionales necesitamos
    extraChars = length % len(key)
    
    #Construir la key resultante
    result = key * repeat + key[:extraChars]
    
    return result

'''
Encriptado y desencriptado Afín
'''
def encrypt(text, key):
    encrypted = ""

    for i in range(len(text)):
        charIndex = alphabet.index(text[i])
        keyIndex = alphabet.index(key[i])
        newIndex = (charIndex + keyIndex) % len(alphabet)
        encrypted += alphabet[newIndex]

    return encrypted

def decrypt(text, key):
    decrypted = ""

    for i in range(len(text)):
        charIndex = alphabet.index(text[i])
        keyIndex = alphabet.index(key[i])
        newIndex = (charIndex - keyIndex) % len(alphabet)
        decrypted += alphabet[newIndex]

    return decrypted

'''
Función principal que maneja la interacción con el usuario.
'''
def main():
    while True:
        #Imprimir menú
        print("\n1. Encriptar")
        print("2. Desencriptar")
        print("3. Salir")
        choice = input("\nSeleccione una opción (1-3): ")
        
        #Salir
        if choice == "3":
            break
        
        #Validar opción
        if choice not in ["1", "2"]:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
            continue
        
        #Obtener texto
        text = input("\nIngrese el texto para encriptar: ")
        text = cleanPlainText(text)
        key = input("Ingrese el texto para encriptar: ")
        key = dinamicKeyGenerator(key, len(text))

        
        #Validar texto
        if not text or not key:
            print("El texto o clave no pueden estar vacías.")
            continue
        
        #Encriptar
        if choice == "1":
            encrypted = encrypt(text, key)
            print(f"\nLlave utilizada: {key}")
            print(f"Texto encriptado: {encrypted}")

        #Desencriptar
        if choice == "2":
            encrypted = decrypt(text, key)
            print(f"\nLlave utilizada: {key}")
            print(f"Texto desencriptado: {encrypted}")

if __name__ == "__main__":
    main()