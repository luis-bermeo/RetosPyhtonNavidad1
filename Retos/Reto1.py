from datetime import datetime

# se pide el nombre del usuario
nombre = input("¡Hola! Cuál es tu nombre? ")

# se obtiene la fecha actual
fecha = datetime.now().strftime("%d/%m/%Y")

# mostramos el saludo navideño
print(f"¡Feliz Navidad, {nombre}! Hoy es {fecha} ! :)")
