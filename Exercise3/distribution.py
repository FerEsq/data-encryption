'''
 * Nombre: distribution.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Creado el 03.02.2025
    - Finalizado el 03.02.2025
'''

from prettytable import PrettyTable
import matplotlib.pyplot as plt

alphabet = "abcdefghijklmnñopqrstuvwxyz"
theoreticalDist = {
    'a': 0.1253, 'b': 0.0142, 'c': 0.0468, 'd': 0.0586, 'e': 0.1368,
    'f': 0.0069, 'g': 0.0101, 'h': 0.0070, 'i': 0.0625, 'j': 0.0044,
    'k': 0.0002, 'l': 0.0497, 'm': 0.0315, 'n': 0.0671, 'ñ': 0.0031,
    'o': 0.0868, 'p': 0.0251, 'q': 0.0088, 'r': 0.0687, 's': 0.0798,
    't': 0.0463, 'u': 0.0393, 'v': 0.0090, 'w': 0.0001, 'x': 0.0022,
    'y': 0.0090, 'z': 0.0052
}

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

#Función para mostrar los resultados
def showResults(frecuencias):
    #Crear la tabla con tres columnas
    table = PrettyTable()
    table.field_names = ["Letra", "Probabilidad Encontrada", "Probabilidad Teórica"]
    
    #Ordenar por frecuencia encontrada de mayor a menor
    frecuencies = dict(sorted(frecuencias.items(),
                            key=lambda x: x[1],
                            reverse=True))
    
    #Agregar filas con ambas probabilidades
    for letter, prob in frecuencies.items():
        table.add_row([letter, f"{prob:.4f}", f"{theoreticalDist[letter]:.4f}"])
    
    print("Análisis comparativo de frecuencias:")
    print(table)
    
    #Crear la gráfica de comparación
    plt.figure(figsize=(15, 8))

    print("\nGráfica de comparación guardada en 'comparison.png'")

    #Preparar datos para la gráfica
    letters = list(alphabet)
    foundProbs = [frecuencies[letra] for letra in letters]
    theoreticalProbs = [theoreticalDist[letra] for letra in letters]
    
    #Crear gráfica de barras
    x = range(len(letters))
    width = 0.35
    
    plt.bar([i - width/2 for i in x], foundProbs, width, label='Frecuencia Encontrada', color='#0A8754')
    plt.bar([i + width/2 for i in x], theoreticalProbs, width, label='Frecuencia Teórica', color='#508CA4')
    
    #Personalizar gráfica
    plt.xlabel('Letras')
    plt.ylabel('Frecuencia')
    plt.title('Comparación de Distribuciones de Frecuencia')
    plt.xticks(x, letters, rotation=45)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    #Ajustar márgenes
    plt.tight_layout()
    
    #Guardar la gráfica
    plt.savefig('Exercise3/comparison.png')
    plt.close()

'''
Análisis de frecuencia
'''
def frecuencyAnalysis(texto):
    #Crear un diccionario para almacenar las frecuencias
    frecuencies = {}
    
    #Contar el total de caracteres (excluyendo espacios y signos de puntuación)
    totalChars = sum(1 for c in texto if c.isalpha())

    for char in alphabet:
        #Contar ocurrencias de cada letra
        count = texto.count(char)
        #Calcular probabilidad (frecuencia relativa)
        prob = count / totalChars if totalChars > 0 else 0
        frecuencies[char] = prob
    
    return frecuencies

'''
Función principal que maneja la interacción con el usuario.
'''
def main():
    while True:
        #Imprimir menú
        print("\n1. Analizar frecuencia")
        print("2. Salir")
        choice = input("\nSeleccione una opción (1 o 2): ")
        
        #Salir
        if choice == "2":
            break
        
        #Validar opción
        if choice not in ["1"]:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
            continue
        
        #Obtener texto
        text = input("\nIngrese el texto para analizar: ")
        text = cleanPlainText(text)
        
        #Validar texto
        if not text:
            print("El texto no puede estar vacío.")
            continue
        
        #Analizar frecuencia
        if choice == "1":
            analysis = frecuencyAnalysis(text)
            showResults(analysis)

if __name__ == "__main__":
    main()