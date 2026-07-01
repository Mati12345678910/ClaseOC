try:
    Po = float(input("Ingresa el precio original: "))
    D = float(input("Ingresa el descuento: "))
    Pd = Po - Po * (D/100)
    print("Su precio con descuento es de ",Pd)
    print("Su descuento es de ", Po-Pd)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
