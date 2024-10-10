print(" ")#espacio a agregar a la ejecucion 
print("Lira Hernandez Dayana Yamileth, 1191, 3W")#datos del realizador
print("Saca la factorial de un numero entero positivo")#esplica lo que hace el codigo
print(" ")#espacio a agregar a la ejecucion

def factorial(n):#define la funcion que sacara la factorial
    resultado = 1 #Inicializamos el resultado en 1, ya que el factorial se multiplica
    for i in range(1, n + 1):
        resultado *= i #Multiplicamos el resultado por cada número hasta n
    return resultado #Devolvemos el resultado final del factorial

#Solicita un número entero positivo al usuario
numero = int(input("Ingresa un entero positivo: "))
# Verificamos si el número ingresado es negativo
if numero < 0:
    print("Por favor, ingresa un número entero positivo.")
#imprime mensaje si el numero es negativo
else:
# Llamamos a la función 'factorial' y mostramos el resultado
    print(f"El factorial de {numero} es {factorial(numero)}")
print(" ")#espacio a agregar a la ejecucion 