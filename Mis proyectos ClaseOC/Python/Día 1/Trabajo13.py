try:
    n1 = float(input("Ingrese un número "))

    if n1 > 0:
        print(n1, " es positivo")
    elif n1 == 0:
        print(n1, " es cero")
    else:
        print(n1, " es negativo")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
