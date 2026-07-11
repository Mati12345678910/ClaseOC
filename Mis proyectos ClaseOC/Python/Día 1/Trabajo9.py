try:
    d = float(input("Ingresa una cantidad de días: "))
    print("Su cantidad en segundos es: ", d*24*60*60)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
