try:
    def CelsAFa(Celsius):
        Fa=(Celsius*9/5)+32
        return Fa
    GrCe=int(input("Ingresa los celisus a convertir "))
    print("Los grados a Farenheit son:", CelsAFa(GrCe))
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
