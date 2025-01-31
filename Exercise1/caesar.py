'''
 * Nombre: caesar.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Creado el 30.01.2025
    - Finalizado el xx.02.2025
'''

alphabet = "abcdefghijklmnñopqrstuvwxyz"

def encrypt(text):
    text = text.lower()
    encrypted = ""
    for char in text:
        for letter in alphabet:
            if char == letter:
                charIndex = alphabet.index(letter)

        newCharIndex = (charIndex + 3) % len(alphabet)
        encrypted += alphabet[newCharIndex]

    return encrypted

def decrypt(text):
    text = text.lower()
    decrypted = ""
    for char in text:
        for letter in alphabet:
            if char == letter:
                charIndex = alphabet.index(letter)

        newCharIndex = (charIndex - 3) % len(alphabet)
        decrypted += alphabet[newCharIndex]

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