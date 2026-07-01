try:
    def contador(palabra):
        largo = len(palabra)
        return largo
    palabra1 = str(input("Ingrese una palabra: "))
    print(contador(palabra1), " caracteres")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
