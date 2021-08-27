saldo = float(input("Dame el saldo del mes anterior: "))
ingresos = float(input("Dame los ingresos: "))
egresos = float(input("Dame los agresos: "))
cheques = int(input("Dame el número de cheques: "))

cuenta = saldo + ingresos - egresos - (cheques * 13)
impuestos = (cuenta * 7.5)/100
total = cuenta - impuestos
print("El saldo final de la cuenta es:",total)