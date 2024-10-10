print(" ")#espacio a agregar a la ejecucion 
print("Lira Hernandez Dayana Yamileth, 1191, 3W")#datos del realizador
print("muestra el argumento mayor que se tomo")#explica lo que hace el codigo
print(" ")#espacio a agregar a la ejecucion
# Función para encontrar el mayor de tres números
def mayor_de_tres(num1, num2, num3):
    """
    Esta función toma tres números como argumentos y devuelve el mayor de ellos.

    Parámetros:
    num1 (float): Primer número
    num2 (float): Segundo número
    num3 (float): Tercer número

    Retorna:
    float: El mayor de los tres números
    """
    # Usamos la función max para encontrar el mayor de los tres números
    return max(num1, num2, num3)
# Solicitar al usuario que ingrese tres números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))
# Llamar a la función para encontrar el mayor número
mayor = mayor_de_tres(numero1, numero2, numero3)
# Mostrar el resultado
print(f"El mayor de los tres números es: {mayor}")
print(" ")#espacio a agregar