# se pide un número para el tamaño del árbol
tamanio = int(input("Ingresa un número para el tamaño del árbol: "))

# se dibuja el árbol
for i in range(1, tamanio + 1):
    print(" " * (tamanio - i) + "*" * (2 * i - 1))

# se hace la base del árbol
print(" " * (tamanio - 1) + "*")

print("Feliz Navidad! :)")
