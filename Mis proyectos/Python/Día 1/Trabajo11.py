try:
    d = float(input("Ingrese el dividendo "))
    di = float(input("Ingrese el divisor "))
    if di == 0:
        print("Error: no se puede dividir por cero")
    else: 
        print("El cociente es: ", d / di)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
