'''
 * Nombre: decryption.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Creado el 05.02.2025
    - Finalizado el 05.02.2025
'''

alphabet = "abcdefghijklmnñopqrstuvwxyz"
theoreticalProbs = {
    'a': 0.11525, 'b': 0.02215, 'c': 0.04019, 'd': 0.05010, 'e': 0.12181,
    'f': 0.00692, 'g': 0.01768, 'h': 0.00703, 'i': 0.06247, 'j': 0.00493,
    'k': 0.00011, 'l': 0.04967, 'm': 0.03157, 'n': 0.06712, 'o': 0.08683,
    'p': 0.02510, 'q': 0.00877, 'r': 0.06871, 's': 0.07977, 't': 0.04632,
    'u': 0.02927, 'v': 0.01138, 'w': 0.00017, 'x': 0.00215, 'y': 0.01008,
    'z': 0.00467, 'ñ': 0.00311
}

'''
Funciones auxiliares
'''
def cleanPlainText(text):
    #Diccionario de reemplazo para caracteres con tilde
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ü': 'u', 'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u'
    }
    
    text = text.lower()
    
    cleanChars = []
    for char in text:
        char = replacements.get(char, char)

        if char in alphabet:
            cleanChars.append(char)

    cleanText = ''.join(cleanChars)
    
    return cleanText

def getFrecuency(text):
    frecuencies = {}
    
    totalChars = sum(1 for c in text if c.isalpha())

    for char in alphabet:
        count = text.count(char)
        prob = count / totalChars if totalChars > 0 else 0
        frecuencies[char] = prob
    
    return frecuencies

def calculateDistance(observed, theoretical):
    #Calcular la distancia entre las frecuencias observadas y teóricas
    distance = 0
    for char in alphabet:
        distance += abs(observed[char] - theoretical[char])
    
    return distance

def checkCoprimes(a, b):
    def mcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return mcd(abs(a), abs(b)) == 1

def modInverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

'''
Fuerza bruta
'''
def decriptKeys(text, a, b):
    """
    Intenta descifrar el texto con valores específicos de a y b.
    """
    try:
        aInv = modInverse(a, len(alphabet))
        if aInv is None:
            return None
        
        decrypted = ""
        for char in text.lower():
            if char in alphabet:
                y = alphabet.index(char)
                newIndex = (aInv * (y - b)) % len(alphabet)
                decrypted += alphabet[newIndex]
            else:
                decrypted += char
        return decrypted
    except:
        return None

def AffineBruteForce(encrypted, aRange=(1,16), bRange=(1,16)):
    results = []

    #Probamos todas las combinaciones posibles de a y b
    for a in range(aRange[0], aRange[1] + 1):
        # Verificamos que 'a' sea coprimo con el tamaño del alfabeto
        if not checkCoprimes(a, len(alphabet)):
            continue
            
        for b in range(bRange[0], bRange[1] + 1):
            decrypted = decriptKeys(encrypted, a, b)
            if decrypted is not None:
                freq = getFrecuency(decrypted)
                distance = calculateDistance(freq, theoreticalProbs)
                results.append((a, b, decrypted, distance))

    #Ordenar por distancia
    results.sort(key=lambda x: x[3])
    
    return results[:1]

def CaesarBruteForce(encrypted, maxRotation=30):
    results = []
    
    #Probamos cada posible rotación hasta max_rotation
    for rotation in range(maxRotation):
        decrypted = ""
        
        for char in encrypted:
            if char in alphabet:
                #Encontramos la posición actual del carácter
                current_index = alphabet.index(char)
                #Calculamos la nueva posición aplicando la rotación
                new_index = (current_index - rotation) % len(alphabet)
                #Añadimos el carácter descifrado
                decrypted += alphabet[new_index]
            else:
                #Mantenemos los caracteres que no están en el alfabeto
                decrypted += char

        freq = getFrecuency(decrypted)
        distance = calculateDistance(freq, theoreticalProbs)

        results.append((rotation, decrypted, distance))   

    #Ordenar por distancia
    results.sort(key=lambda x: x[2])
    
    return results[:1]

'''
Función principal que maneja la interacción con el usuario.
'''
def main():
    try:
        with open('Affine/cipher.txt', 'r', encoding='utf-8') as archivo:
            text = archivo.read()
    except FileNotFoundError:
        print("El archivo no se encontró")
    except IOError:
        print("Error al leer el archivo")

    #Limpiar el texto
    text = cleanPlainText(text)

    results = AffineBruteForce(text)

    print("Posible texto descifrado:\n")
    for i, (a, b, decrypted, distance) in enumerate(results, 1):
        print(f"Claves: a={a}, b={b}")
        print(f"Distancia: {distance:.4f}")
        print("Texto descifrado:")
        print(decrypted)

if __name__ == "__main__":
    main()