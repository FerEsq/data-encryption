'''
 * Nombre: script7.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Finalizado el 28.01.2025
'''

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
Función principal que maneja la interacción con el usuario.
'''
def main():
    while True:
        #Imprimir menú
        print("\n1. Generar una key dinámica")
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
        key = input("\nIngrese la key: ")
        len = input("Ingrese la longitud de la key: ")
        
        #Validar texto
        if not len or not len.isdigit():
            print("La longitud no es válida")
            continue
        elif not key:
            print("La key no puede estar vacía")
            continue
        elif int(len) < 1:
            print("La longitud debe ser mayor a 0")
            continue
        
        #Convertir a binario
        if choice == "1":
            key = dinamicKeyGenerator(key, int(len))
            print(f"\nKey de longitud {len}: {key}")        

if __name__ == "__main__":
    main()
