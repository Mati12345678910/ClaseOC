try:

    anio_viejot = input("¿En qué año naciste? ")
    anio_viejon = int(anio_viejot)
    anio_ahora = 2026
    edad_tu = anio_ahora - anio_viejon
    print("Tu edad es: ",edad_tu)
    if edad_tu > 17:
        print("Tú ser mayor de edad")
    elif edad_tu == 14:
        print("Prende cam")
    else:
        print("Eres menor de edad")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
