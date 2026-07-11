try:
    a = float(input("Ingresa tu altura "))
    p = float(input("Ingresa tu peso "))
    imc = p / (a*a)
    print ("Tu imc es de ",imc)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
except ZeroDivisionError:
    print("❌ Error: No se puede dividir por cero.")
