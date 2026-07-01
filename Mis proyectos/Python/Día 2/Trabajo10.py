try:
    contraSec= "Guideon123"
    contr= input("Ingresa la contraseña ")
    while contr != contraSec:
        contr= input("Intenta de nuevo ")
    print("¡Bienvenido!")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")

