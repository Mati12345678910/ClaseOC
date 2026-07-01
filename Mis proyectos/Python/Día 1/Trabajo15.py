try:
    C = str("Guideon123")
    Cd = input("Ingrese la contraseña: ")
    if C == Cd:
        print("Acceso concedido")
    else:
        print("Acceso denegado")
except ValueError:
    print("No se puede, riesgo de explosión")