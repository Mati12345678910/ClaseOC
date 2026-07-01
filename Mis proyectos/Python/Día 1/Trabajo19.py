try:
    ns = 2
    ne = int(input("Ingresa un número del 1 al 10 "))
    if ne == ns:
        print("Ganaste")
    else:
        print("Intenta de nuevo")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
