try:

    nument = int(input("Ingresa un número entero "))
    if nument % 2 == 0:
        print("Tu número es par")
    else:
        print("Tu número es impar")
except ValueError:
    #Guideon&Gongion were here
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")