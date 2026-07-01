try: 
    Nota1 = float(input("Ingresa la primer nota "))
    Nota2 = float(input("Ingresa la segunda nota "))
    Nota3 = float(input("Ingresa la tercera nota "))
    print("El promedio de esas 3 notas es: ",(Nota1+Nota2+Nota3)/3)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
