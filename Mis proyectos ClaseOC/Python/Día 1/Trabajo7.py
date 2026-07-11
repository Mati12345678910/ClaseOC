try:
    GC = float(input("Ingresa la cantidad de grados Celsius "))
    GF = (GC*(9/5))+32
    print("La temperatura en Farenheit es ", GF)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
