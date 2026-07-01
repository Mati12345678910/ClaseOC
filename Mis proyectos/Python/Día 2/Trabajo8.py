try:
    cuenta=11
    while cuenta != 1:
        cuenta = cuenta-1
        print(cuenta)
    print("¡Despegue!")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
