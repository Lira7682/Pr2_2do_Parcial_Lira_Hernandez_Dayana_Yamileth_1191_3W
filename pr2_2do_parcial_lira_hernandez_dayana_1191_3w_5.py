print(" ")#espacio a agregar a la ejecucion 
print("Lira Hernandez Dayana Yamileth, 1191, 3W")#datos del realizador
print("muestra el area de un circulo y volumen de una esfera")#explica lo que hace el codigo
print(" ")#espacio a agregar a la ejecucion

import math  # Importamos el módulo math para acceder a funciones matemáticas
# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * radio ** 2  # Fórmula: π * r²
# Función para calcular el volumen de una esfera
def volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3  # Fórmula: (4/3) * π * r³
# Solicitar al usuario que ingrese el radio
radio = float(input("Ingresa el radio del círculo/esfera: "))
# Calcular el área del círculo y el volumen de la esfera
area = area_circulo(radio)  # Llamamos a la función para calcular el área
volumen = volumen_esfera(radio)  # Llamamos a la función para calcular el volumen
# Mostrar los resultados
print(f"El área del círculo es: {area:.2f}")#Imprimimos el área formateada a dos decimales
print(f"El volumen de la esfera es: {volumen:.2f}")
#Imprimimos el volumen formateado a dos decimales
print(" ")#espacio a agregar a la ejecucion