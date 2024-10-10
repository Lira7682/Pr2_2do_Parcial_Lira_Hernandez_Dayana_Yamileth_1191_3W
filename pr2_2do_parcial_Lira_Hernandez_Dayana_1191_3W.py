print(" ")#espacio a agregar a la ejecucion 
print("Lira Hernandez Dayana Yamileth, 1191, 3W")#datos del 
print("Saluda al usuario cuantas veces lo pida")
print(" ")#espacio a agregar a la ejecucion

def saludar():#define la funcion
    print("Hey amigos!")#imprime el saludo a ejecutar

# Inicia un bucle infinito para que el programa siga solicitando al usuario.
while True:
    user_input = input("Escribe 'saludar' para ver el saludo o 'salir' para terminar: ")
#verifica q el usuario ingreso "saludar"
    if user_input.lower() == 'saludar':
        saludar()#Se llama a la función 'saludar' para mostrar el saludo.
    # Verificamos si el usuario escribió 'salir'
    elif user_input.lower() == 'salir':
        print("¡Hasta luego!")# Imprimimos un mensaje de despedida.
        break  # Salimos del bucle para terminar el programa.
print(" ")#espacio a agregar a la ejecucion

