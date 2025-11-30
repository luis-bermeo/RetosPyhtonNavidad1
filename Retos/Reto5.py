# lista vacía para los deseos
deseos = []

print("Escribe tus deseos navideños (escribe 'fin' para terminar):")

while True:
    deseo = input("--> Deseo: ")
    if deseo.lower() == "fin":
        break
    deseos.append(deseo)

# se ordenan los deseos
deseos.sort()

# guardamos los deseos en un archivo wishlist.txt
with open("wishlist.txt", "w") as archivo:
    for d in deseos:
        archivo.write(d + "\n")

# mostramos los resultados
print(f"\nHas introducido {len(deseos)} deseos:")
for d in deseos:
    print(f" - {d}")
