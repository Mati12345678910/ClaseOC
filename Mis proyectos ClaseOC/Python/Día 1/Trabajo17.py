try:
    nc = input("Ingresa el nombre de tu ciudad ")
    nm = input("Ingresa el nombre de tu mascota ")
    nb = nc + " " + nm 
    print("El nombre de tu banda de rock es: ", nb)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")