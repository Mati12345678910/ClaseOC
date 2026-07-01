try:

    Ondo = 0.25
    Ena = Ondo * 4
    CantidadOndos = float(input("Ingresa la canidad de Enas a Ondos "))
    CantidadEna = CantidadOndos * 0.25
    print(CantidadEna,"enas , es igual a,", CantidadOndos, "ondos")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
