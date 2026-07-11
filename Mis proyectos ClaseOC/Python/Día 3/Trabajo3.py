try:
    def EsPar(numero):
        resultado=numero%2
        if resultado == 0:
            print("es par")
        else:
            print("es impar")
    NumEle=int(input("Ingresa un número "))
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
except ZeroDivisionError:
    print("❌ Error: No se puede dividir por cero.")
