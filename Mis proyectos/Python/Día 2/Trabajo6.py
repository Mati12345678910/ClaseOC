try:
    agenda = {

        "Guideon": "+54 9 11 5109 3319",
        "Gongion": "+54 9 11 3208 4803",
        "Gandeon": "+54 9 11 3319 5109",
    }
    ValorPedido = input("Solicita un nombre o teléfono ")
    print(agenda.get(ValorPedido))
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
