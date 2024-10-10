print(" ")#espacio a agregar a la ejecucion 
print("Lira Hernandez Dayana Yamileth, 1191, 3W")#datos del realizador
print("muestra la distancia entre dos puntos")#explica lo que hace el codigo
print(" ")#espacio a agregar a la ejecucion
# Función para calcular la distancia dirigida entre dos puntos
def distancia_dirigida(punto1, punto2):
    """
    Esta función calcula la distancia dirigida entre dos puntos en el plano cartesiano.

    Parámetros:
    punto1 (tuple): Coordenadas del primer punto (x1, y1)
    punto2 (tuple): Coordenadas del segundo punto (x2, y2)

    Retorna:
    tuple: Distancia dirigida en las coordenadas (dx, dy)
    """
    # Desempaquetamos las coordenadas de los puntos
    x1, y1 = punto1
    x2, y2 = punto2
    
    # Calculamos la distancia dirigida en x y en y
    dx = x2 - x1  # Distancia dirigida en x
    dy = y2 - y1  # Distancia dirigida en y
    
    return (dx, dy)  # Retornamos las distancias dirigidas como un tuple
# Solicitar al usuario que ingrese las coordenadas del primer punto
x1 = float(input("Ingresa la coordenada x del primer punto: "))
y1 = float(input("Ingresa la coordenada y del primer punto: "))
punto1 = (x1, y1)  # Creamos un tuple para el primer punto
# Solicitar al usuario que ingrese las coordenadas del segundo punto
x2 = float(input("Ingresa la coordenada x del segundo punto: "))
y2 = float(input("Ingresa la coordenada y del segundo punto: "))
punto2 = (x2, y2)  # Creamos un tuple para el segundo punto
# Llamar a la función para calcular la distancia dirigida
distancia = distancia_dirigida(punto1, punto2)
# Mostrar el resultado
print(f"La distancia dirigida entre los puntos es: dx = {distancia[0]}, dy = {distancia[1]}")
print(" ")#espacio a agregar a la ejecucion