try:
    n1 = float(input("Ingrese tu nota "))

    if 10 >= n1 >= 6:
        print("Aprobado")
    elif 6 > n1 >= 0:
        print("Desaprobado")
    else:
        print("Error")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
