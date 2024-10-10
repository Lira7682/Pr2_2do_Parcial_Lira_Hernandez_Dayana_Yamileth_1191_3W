print(" ")#espacio a agregar a la ejecucion 
print("Lira Hernandez Dayana Yamileth, 1191, 3W")#datos del realizador
print("Muestra la cantidad sin iva, con iva y la factura")#explica lo que hace el codigo
print(" ")#espacio a agregar a la ejecucion

#Definimos una clase para manejar la factura
class Factura:
    def __init__(self, cantidad_sin_iva, porcentaje_iva):
        self.cantidad_sin_iva = cantidad_sin_iva  # Almacena la cantidad sin IVA
        self.porcentaje_iva = porcentaje_iva  # Almacena el porcentaje de IVA

    # Método para calcular el total de la factura
    def calcular_total(self):
        # Calculamos el IVA
        iva = self.cantidad_sin_iva * (self.porcentaje_iva / 100)
        # Calculamos el total sumando la cantidad sin IVA y el IVA
        total = self.cantidad_sin_iva + iva
        return total  # Devolvemos el total de la factura

# Solicitar al usuario que ingrese la cantidad sin IVA
cantidad_sin_iva = float(input("Ingresa la cantidad sin IVA: "))

# Solicitar al usuario que ingrese el porcentaje de IVA
porcentaje_iva = float(input("Ingresa el porcentaje de IVA a aplicar: "))

# Crear una instancia de la clase Factura
factura = Factura(cantidad_sin_iva, porcentaje_iva)

# Calcular el total de la factura
total_factura = factura.calcular_total()

# Mostrar el resultado final formateado a dos decimales
print(f"El total de la factura después de aplicar el IVA es: {total_factura:.2f}")
print(" ")
