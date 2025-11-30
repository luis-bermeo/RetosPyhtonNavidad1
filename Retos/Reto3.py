villancicos = {
    "1": "🎵 Noche de paz, noche de amor...",
    "2": "🎵 Campana sobre campana...",
    "3": "🎵 Los peces en el río...",
    "4": "🎵 Blanca Navidad..."
}

while True:
    print("\n Bienvenido al Menú de villancicos:")
    for clave in villancicos:
        print(f"{clave}. Villancico {clave}")
    print("5. SALIR")

    opcion = input("Elige un villancico: ")

    if opcion == "5":
        print("¡Hasta pronto! 🎅")
        break
    elif opcion in villancicos:
        print(villancicos[opcion])
    else:
        print("Opción no válida ❌")
