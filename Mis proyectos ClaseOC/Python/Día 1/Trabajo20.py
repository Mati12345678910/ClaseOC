try:
    p = "piedra"
    e = input("Elige entre piedra, papel o tijera ")
    if p == e:
        print("Empate")
    elif e == "tijera":
        print("Perdiste. Piedra rompe tijera")
    elif e == "papel":
        print("¡Ganaste! Papel envuelve piedra")
    else:
        print("Error")
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")