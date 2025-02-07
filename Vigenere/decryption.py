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

def dinamicKeyGenerator(key, length):    
    if length == 0:
        return ""
    repeat = length // len(key)
    extraChars = length % len(key)
    result = key * repeat + key[:extraChars]
    return result

'''
Fuerza bruta
'''
def decrypt(text, key):
    decrypted = ""
    key_idx = 0 
    for char in text:
        if char in alphabet:
            charIndex = alphabet.index(char)
            keyIndex = alphabet.index(key[key_idx])
            newIndex = (charIndex - keyIndex) % len(alphabet)
            decrypted += alphabet[newIndex]
            key_idx = (key_idx + 1) % len(key)
        else:
            decrypted += char
    return decrypted

def generateDecryptKeys(prefix="pa", minLength=2, maxLength=6):
    possibleKeys = []
    
    #Si el prefijo es más largo que max_length, lo cortamos
    if len(prefix) > maxLength:
        return [prefix[:maxLength]]
    
    #Si el prefijo ya tiene la longitud mínima, lo añadimos
    if len(prefix) >= minLength:
        possibleKeys.append(prefix)
    
    #Si ya alcanzamos la longitud máxima, no seguimos expandiendo
    if len(prefix) == maxLength:
        return possibleKeys
    
    #Generamos todas las posibles combinaciones añadiendo letras del alfabeto
    for char in alphabet:
        newPrefix = prefix + char
        if len(newPrefix) <= maxLength:
            possibleKeys.extend(generateDecryptKeys(newPrefix, minLength, maxLength))
    
    return possibleKeys

def VigenereBruteForce(encrypted, prefix="pa", minLength=2, maxLength=6):
    results = []
    attempts = 0
    
    # Generamos todas las posibles claves
    possibleKeys = generateDecryptKeys(prefix, minLength, maxLength)
    total_keys = len(possibleKeys)
    
    print(f"\nTotal de claves a probar: {total_keys}")
    print("Iniciando descifrado...\n")
    
    # Para cada clave posible, intentamos descifrar
    for key in possibleKeys:
        attempts += 1
        
        # Cada 10,000 intentos, mostramos el progreso
        if attempts % 50000 == 0:
            progress = (attempts / total_keys) * 100
            print(f"Progreso: {attempts:,}/{total_keys:,} claves probadas ({progress:.2f}%)")
        
        # Generamos la clave dinámica del tamaño necesario
        dynamicKey = dinamicKeyGenerator(key, len(encrypted))
        # Intentamos descifrar
        decrypted = decrypt(encrypted, dynamicKey)
        freq = getFrecuency(decrypted)
        distance = calculateDistance(freq, theoreticalProbs)
        # Guardamos el resultado
        results.append((key, dynamicKey, decrypted, distance))

    # Ordenamos por distancia
    results.sort(key=lambda x: x[3])
    
    print(f"\nDescifrado completado. Se probaron {attempts:,} claves.\n")
    
    return results

'''
Función principal que maneja la interacción con el usuario.
'''
def main():
    try:
        with open('Vigenere/cipher.txt', 'r', encoding='utf-8') as archivo:
            text = archivo.read()
    except FileNotFoundError:
        print("El archivo no se encontró")
        return
    except IOError:
        print("Error al leer el archivo")
        return

    # Limpiar el texto
    text = cleanPlainText(text)

    print("Iniciando fuerza bruta...")
    results = VigenereBruteForce(text)

    print("Top 5 resultados más probables:\n")
    for i, (key, dynamicKey, decrypted, distance) in enumerate(results[:15], 1):
        print(f"#{i}")
        print(f"Clave: {key}")
        print(f"Texto descifrado: {decrypted[:100]}..." if len(decrypted) > 100 else decrypted)
        print(f"Distancia: {distance:.6f}\n")

if __name__ == "__main__":
    main()