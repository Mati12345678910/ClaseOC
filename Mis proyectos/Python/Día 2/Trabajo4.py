try:
    contador=0
    palabra = input("Elige una palabra ")
    for vocales in palabra:
        if vocales in "aáAÁeéEÉiíIÍoóOÓúuUÚ":
            contador = contador+1
    print("Tu palabra tiene ", contador, " vocal/es")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
