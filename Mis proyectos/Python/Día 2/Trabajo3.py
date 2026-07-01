try:
    numero = int(input("Ingresa el número que quieres ver su tabla de multiplicar: "))
    for num in range(1,11):
        tabla = numero*num
        print(tabla)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")