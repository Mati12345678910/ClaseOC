try:
    def mayorde(n1,n2,n3):
        if n1 > n2 and n1 > n3:
            return n1
        elif n2 > n1 and n2 > n3:
            return n2
        else:
            return n3
    Numeleg1=int(input("Elige el primer número "))
    Numeleg2=int(input("Elige el segundo número "))
    Numeleg3=int(input("Elige el tercero número "))
    print(mayorde(Numeleg1,Numeleg2,Numeleg3))
except ValueError:
    print("❌ Error: ¡Debes escribir un NÚMERO, no letras!")
