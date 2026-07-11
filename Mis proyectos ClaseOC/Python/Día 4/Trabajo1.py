pinV = "LaDobleG"
MontoaRetirar=0
saldo = 1000
NuevoSaldo=1000
ingreso = False
pinDado = input("Ingrese el PIN: ")
while pinDado != pinV:
    pinDado = input("Ingrese el PIN: ")
def retirar(monto):
    if saldo - monto >= 0:
         NuevoSaldo = saldo - monto
         return(NuevoSaldo)
try:
        MontoaRetirar = int(input("Ingrese una cantidad a retirar: "))
except ValueError:
        print("Ingrese un monto valido")
NuevoSaldo=retirar(MontoaRetirar)
if NuevoSaldo == None:
    print("No tienes saldo suficiente")
else:
    print("Tu saldo es de", NuevoSaldo)