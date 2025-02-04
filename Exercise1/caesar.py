'''
 * Nombre: caesar.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Creado el 30.01.2025
    - Finalizado el 02.02.2025
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
        if char.isalpha() or char.isspace():
            cleanChars.append(char)
    
    cleanText = ''.join(cleanChars)
    
    return cleanText

'''
Encriptado y desencriptado César
'''
def encrypt(text):
    encrypted = ""
    for char in text:
        #Si el carácter está en el alfabeto, lo encriptamos
        if char in alphabet:
            charIndex = alphabet.index(char)
            newCharIndex = (charIndex + 3) % len(alphabet)
            encrypted += alphabet[newCharIndex]
        else:
            #Si no está en el alfabeto, lo mantenemos igual
            encrypted += char

    return encrypted

def decrypt(text):
    decrypted = ""
    for char in text:
        #Si el carácter está en el alfabeto, lo desencriptamos
        if char in alphabet:
            charIndex = alphabet.index(char)
            newCharIndex = (charIndex - 3) % len(alphabet)
            decrypted += alphabet[newCharIndex]
        else:
            #Si no está en el alfabeto, lo mantenemos igual
            decrypted += char

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
        
        #Validar texto
        if not text:
            print("El texto no puede estar vacío.")
            continue
        
        #Encriptar
        if choice == "1":
            encrypted = encrypt(text)
            print(f"\nTexto encriptado: {encrypted}")

        #Desencriptar
        if choice == "2":
            encrypted = decrypt(text)
            print(f"\nTexto desencriptado: {encrypted}")

if __name__ == "__main__":
    main()