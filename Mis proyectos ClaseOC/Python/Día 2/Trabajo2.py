try:
    notas = [1,2,3,4,5,6,7,8,9,10]
    for num in range(1):
        suma = sum(notas)
        promedio = suma / len(notas)
    print("El promedio de las notas es: ", promedio)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
except ZeroDivisionError:
    print("❌ Error: No se puede dividir por cero.")