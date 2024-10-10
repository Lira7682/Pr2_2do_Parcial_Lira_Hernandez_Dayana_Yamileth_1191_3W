print(" ")#espacio a agregar a la ejecucion 
print("Lira Hernandez Dayana Yamileth, 1191, 3W")#datos del realizador
print("suma y multiplica numeros de una lista")#explica lo que hace el codigo
print(" ")#espacio a agregar a la ejecucion
# Función para sumar todos los números de una lista
def sum(lista):
    """
    Esta función toma una lista de números y devuelve la suma de todos ellos.

    Parámetros:
    lista (list): Lista de números

    Retorna:
    float: La suma de los números en la lista
    """
    total = 0  # Inicializamos el total en 0
    for num in lista:  # Iteramos sobre cada número en la lista
        total += num  # Sumamos el número al total
    return total  # Devolvemos el total de la suma
# Función para multiplicar todos los números de una lista
def multip(lista):
    """
    Esta función toma una lista de números y devuelve el producto de todos ellos.

    Parámetros:
    lista (list): Lista de números

    Retorna:
    float: El producto de los números en la lista
    """
    producto = 1  # Inicializamos el producto en 1
    for num in lista:  # Iteramos sobre cada número en la lista
        producto *= num  # Multiplicamos el número al producto
    return producto  # Devolvemos el producto total
# Ejemplo de uso
numeros = [1, 2, 3, 4]  # Lista de números
# Llamar a la función sum para obtener la suma
resultado_suma = sum(numeros)
print(f"La suma de la lista es: {resultado_suma}")  # Imprimir el resultado de la suma
# Llamar a la función multip para obtener el producto
resultado_multip = multip(numeros)
print(f"La multiplicación de la lista es: {resultado_multip}")
#Imprimir el resultado de la multiplicación
print(" ")#espacio a agregar a la ejecucion
