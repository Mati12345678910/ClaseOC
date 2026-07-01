try:
    lista_compras=[]
    for guideon in range(5):
        productos = input("añade un elemento ")
        lista_compras.append(productos)
    print("La lista quedo así: ",lista_compras)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
