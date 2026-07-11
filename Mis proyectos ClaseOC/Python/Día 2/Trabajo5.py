try:
    listaNum=[1,65,234,87,67,76,341,4,89,23]
    for num in listaNum:
        if num % 2 == 0:
            print("El número ", num, " es par")   
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
except ZeroDivisionError:
    print("❌ Error: No se puede dividir por cero.")