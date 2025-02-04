'''
 * Nombre: frecuency.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Creado el 03.02.2025
    - Finalizado el 03.02.2025
'''

from prettytable import PrettyTable

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

#Función para mostrar los resultados de manera ordenada
def showResults(frecs):
    #Ordenar por frecuencia de mayor a menor
    frecuencies = dict(sorted(frecs.items(), 
                                        key=lambda x: x[1], 
                                        reverse=True))

    #Crear la tabla
    table = PrettyTable()
    table.field_names = ["Letra", "Probabilidad"]

    #Agregar filas con los datos
    for letter, prob in frecuencies.items():
        table.add_row([letter, f"{prob:.4f}"])

    # Imprimir la tabla
    print("Análisis de frecuencia de caracteres:")
    print(table)

'''
Análisis de frecuencia
'''
def frecuencyAnalysis(text):
    #Crear un diccionario para almacenar las frecuencias
    frecuencies = {}
    
    #Contar el total de caracteres (excluyendo espacios y signos de puntuación)
    totalChars = sum(1 for c in text if c.isalpha())

    for char in alphabet:
        #Contar ocurrencias de cada letra
        count = text.count(char)
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