try:
    Ht = float(input("Ingresa la cantidad de horas mensuales trabajadas: "))
    Th = float(input("Ingresa la tarifa por hora "))
    Gm = Ht*Th
    print("Tu salario mensual es de ", Gm)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
