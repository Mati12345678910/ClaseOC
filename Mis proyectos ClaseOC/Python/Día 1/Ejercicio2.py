try:

    conto = float(input("Ingresa il conto perfavore "))
    porprop = float(input("¿Qúe porcentaje de propina quiere dedicarle al señor mesero llamado Luigi? "))
    contofinale = conto * (porprop / 100) + conto
    print("Il tuo conto finale è: ", contofinale)
    print("La mancia da pagare è: ", contofinale-conto)
except ValueError:
    print("❌ Error: ¡Debes escribir unos NÚMERO, no letras!")
