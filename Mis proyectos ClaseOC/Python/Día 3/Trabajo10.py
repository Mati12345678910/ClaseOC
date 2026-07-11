try:
    def votarver(edad):
        if edad >= 18:
            print("Puedes votar")
        else:
            print("No puedes votar ")
    edaddada=int(input("Ingresa tu edad "))
    votarver(edaddada)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")