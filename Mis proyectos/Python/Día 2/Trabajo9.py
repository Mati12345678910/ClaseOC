try:
    precios = {
        "Manzana": 100,
        "Banana": 50,
        "Naranja": 80,
    }
    fruta = input("¿Qué fruta desea comprar, estimado? ")
    fruta1 = precios.get(fruta)
    kilos = int(input("¿Cuántos kilogramos de dicha fruta desea, señor? "))
    print("El valor total de su compra sería de: ",fruta1*kilos) 
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
