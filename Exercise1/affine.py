'''
 * Nombre: affine.py
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

def checkCoprimes(a, b):
    def mcd(a, b):
        #Calculo del Máximo Común Divisor usando el algoritmo de Euclides
        while b:
            a, b = b, a % b
        return a
    
    return mcd(abs(a), abs(b)) == 1

def modInverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
        
    return None  #No tiene inverso si no son coprimos

'''
Encriptado y desencriptado Afín
'''
def encrypt(text, a, b):
    if checkCoprimes(a, len(alphabet)) != 1:
        raise ValueError(f"El valor de 'a' debe ser coprimo con el tamaño del alfabeto ({len(alphabet)})")
    
    encrypted = ""

    for char in text:
        x = alphabet.index(char)
        newIndex = (a * x + b) % len(alphabet)
        encrypted += alphabet[newIndex]

    return encrypted

def decrypt(text, a, b):
    a_inv = modInverse(a, len(alphabet))
    if a_inv is None:
        raise ValueError(F"No se puede calcular el inverso de 'a'. Debe ser coprimo con el tamaño del alfabeto ({len(alphabet)})")

    decrypted = ""

    for char in text:
        y = alphabet.index(char)
        newIindex = (a_inv * (y - b)) % len(alphabet)
        decrypted += alphabet[newIindex]

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
        a = int(input("Ingrese el valor de 'a': "))
        b = int(input("Ingrese el valor de 'b': "))
        
        #Validar texto
        if not text or a == 0 or b == 0:
            print("El texto o las claves no puede estar vacías.")
            continue
        
        #Encriptar
        if choice == "1":
            encrypted = encrypt(text, a, b)
            print(f"\nTexto encriptado: {encrypted}")

        #Desencriptar
        if choice == "2":
            encrypted = decrypt(text, a, b)
            print(f"\nTexto desencriptado: {encrypted}")

if __name__ == "__main__":
    main()