try:
    import random
    SecNum= random.randint(1,100)
    adv = False
    print("🤖 He pensado un número del 1 al 100. ¿Puedes adivinarlo?")
    while adv == False:
        NumEle=int(input("Haz tu adivinación "))
        if NumEle == SecNum:
            adv = True
        elif NumEle > SecNum:
            print("El número es menor")
            print("Intenta de nuevo")
        else:
            print("El número es mayor")
            print("Intenta de nuevo")
    print("Has ganado")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
