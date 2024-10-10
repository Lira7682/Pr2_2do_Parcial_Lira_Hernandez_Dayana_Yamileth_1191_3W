print(" ")#espacio a agregar a la ejecucion 
print("Lira Hernandez Dayana Yamileth, 1191, 3W")#datos del realizador
print("Captura dirección de email")#esplica lo que hace el codigo
print(" ")#espacio a agregar a la ejecucion
# Función para verificar si la dirección de email es válida
def es_email_valido(email):
    # Comprobamos si el símbolo '@' está presente en la dirección de email
    return '@' in email  # Devuelve True si '@' está en el email, de lo contrario False
# Solicitar al usuario que ingrese su dirección de email
email = input("Por favor, ingresa tu dirección de email: ")
# Llamar a la función para verificar si el email es válido
if es_email_valido(email):
    # Si la función devuelve True, el email es válido
    print("La dirección de email es válida.")
else:
    # Si la función devuelve False, el email no es válido
    print("La dirección de email no es válida. Asegúrate de que contenga '@'.")
print(" ")#espacio a agregar a la ejecucion