print(" ")#espacio a agregar a la ejecucion 
print("Lira Hernandez Dayana Yamileth, 1191, 3W")#datos del realizador
print("verifica si un carácter es una vocal")#explica lo que hace el codigo
print(" ")#espacio a agregar a la ejecucion
# Función para verificar si un carácter es una vocal
def es_vocal(caracter):
    """
    Esta función toma un carácter y devuelve True si es una vocal, 
    de lo contrario devuelve False.

    Parámetros:
    caracter (str): Un carácter a verificar

    Retorna:
    bool: True si el carácter es una vocal, False en caso contrario
    """
    # Definimos las vocales en minúsculas y mayúsculas
    vocales = 'aeiouAEIOU'  
    # Comprobamos si el carácter está en la cadena de vocales
    return caracter in vocales  # Devuelve True si es vocal, False si no
# Solicitar al usuario que ingrese un carácter
caracter = input("Por favor, ingresa un carácter: ")
# Verificamos que el usuario solo haya ingresado un único carácter
if len(caracter) == 1:
    # Llamar a la función para verificar si el carácter es una vocal
    resultado = es_vocal(caracter)
    # Mostrar el resultado
    if resultado:
        print(f"El carácter '{caracter}' es una vocal.")
    else:
        print(f"El carácter '{caracter}' no es una vocal.")
else:
    print("Por favor, ingresa solo un carácter.")
print(" ")#espacio a agregar a la ejecucion
