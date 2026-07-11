try:

    BR = int(input("Ingresa la base del rectángulo 2"))
    AR = int(input("Ingresa la altura del rectángulo "))
    print("El área del rectángulo es: ",BR*AR)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
