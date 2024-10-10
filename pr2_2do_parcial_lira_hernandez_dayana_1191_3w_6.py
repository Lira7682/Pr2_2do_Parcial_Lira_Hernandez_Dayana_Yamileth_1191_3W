print(" ")#espacio a agregar a la ejecucion 
print("Lira Hernandez Dayana Yamileth, 1191, 3W")#datos del realizador
print("Volumen de un Cilindro Utilizando el Área del Círculo")#explica lo que hace el codigo
print(" ")#espacio a agregar a la ejecucion
import math  # Importamos el módulo math para acceder a funciones matemáticas
# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * radio ** 2  # Fórmula: π * r²
# Función para calcular el volumen de un cilindro
def volumen_cilindro(radio, altura):
    area_base = area_circulo(radio)  # Llamamos a la función para obtener el área de la base
    return area_base * altura  # Fórmula: área de la base * altura
# Solicitar al usuario que ingrese el radio y la altura
radio = float(input("Ingresa el radio de la base del cilindro: "))  # Pedimos el radio
altura = float(input("Ingresa la altura del cilindro: "))  # Pedimos la altura
# Calcular el volumen del cilindro
volumen = volumen_cilindro(radio, altura)  # Llamamos a la función para calcular el volumen
# Mostrar el resultado
print(f"El volumen del cilindro es: {volumen:.2f}")
#Imprimimos el volumen formateado a dos decimales
print(" ")#espacio a agregar a la ejecucion