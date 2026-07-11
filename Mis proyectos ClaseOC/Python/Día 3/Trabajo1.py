try:
    def saludar_amigo(nombre):
        print(f"¡Hola {nombre}!")
    nombre_amigo=input("Nombra un amigo ")
    saludar_amigo(nombre_amigo)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
