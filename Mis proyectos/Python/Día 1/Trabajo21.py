try:
    nombre = input("Ingresa tu nombre ")
    ciudad = input("Ingresa tu ciudad ")
    print("Hola ", nombre," bienvenido a ", ciudad,". ¡Espero que disfrutes el curso!")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
