try:
    def email(nombre,apellido):
        print(f"{nombre}.{apellido}@ipm.edu.ar")
    nombredado= input("Dí tu nombre ").lower()
    apellidodado=input("Dí tu apellido ").lower()
    email(nombredado,apellidodado)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")