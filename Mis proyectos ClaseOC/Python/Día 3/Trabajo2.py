try:
    def Cuadración(número):
        Cuadrado=número*número
        return Cuadrado
    NumEle=int(input("Ingresa un número "))
    print(f"El cuadrado de tu número es: {Cuadración(NumEle)}")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")