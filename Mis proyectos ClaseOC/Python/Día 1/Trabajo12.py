try:
    n1 = float(input("Ingrese un número "))
    n2 = float(input("Ingrese otro número "))
    if n1 > n2:
        print("El número mayor es: ",n1)
    elif n1 == n2:
        print("Ambos números son iguales")
    else:
        print("El número mayor es: ",n2)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
