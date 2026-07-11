try:
    suma_total = 0
    numeroIngresado=1
    while numeroIngresado != 0:
        numeroIngresado = int(input("Ingresa un número "))
        suma_total = numeroIngresado+suma_total
    print("La suma total dió:",suma_total)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
