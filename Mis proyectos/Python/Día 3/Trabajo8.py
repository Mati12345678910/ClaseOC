try:
    def descuento(precio,descuento):
        precioT=precio - precio*descuento
        return precioT
    preciodado=float(input("Ingresa un precio "))
    descuentodado= float(input("Ingresa un descuento "))
    print("El precio final es de:",descuento(preciodado,descuentodado))
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
