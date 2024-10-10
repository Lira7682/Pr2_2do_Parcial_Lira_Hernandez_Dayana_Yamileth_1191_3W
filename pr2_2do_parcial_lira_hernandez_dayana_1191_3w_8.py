print(" ")#espacio a agregar a la ejecucion 
print("Lira Hernandez Dayana Yamileth, 1191, 3W")#datos del realizador
print("muestra la longitud de una palabra")#explica lo que hace el codigo
print(" ")#espacio a agregar a la ejecucion
# Función para calcular la longitud de la última palabra en un string
def longitud_ultima_palabra(frase):
    # Eliminamos los espacios en blanco al inicio y al final del string
    frase = frase.strip()
    # Dividimos la frase en palabras utilizando espacios como separadores
    palabras = frase.split()
    # Verificamos si hay palabras en la lista
    if palabras:
        # Retornamos la longitud de la última palabra
        return len(palabras[-1])  # '[-1]' accede a la última palabra de la lista
    else:
        return 0  # Si no hay palabras, retornamos 0
# Solicitar al usuario que ingrese una frase
frase = input("Por favor, ingresa una frase: ")
# Llamar a la función para calcular la longitud de la última palabra
longitud = longitud_ultima_palabra(frase)
# Mostrar el resultado
print(f"La longitud de la última palabra es: {longitud}")
print(" ")#espacio a agregar a la ejecucion