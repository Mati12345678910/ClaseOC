try:
    def MinutosHoras(CMin):
        CHoras = CMin//60
        Cminutos = CMin%60
        print(f"{CHoras} horas con {Cminutos} minutos")
    MinutosD=int(input("Da una cantidad de minutos "))
    MinutosHoras(MinutosD)
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
