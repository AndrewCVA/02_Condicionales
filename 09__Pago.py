'''
Programa que permita a un usuario tomar una decisión del tipo
de pago a usar. Si la cuenta es menor a $150000 pago en efectivo.
Si no, si es de $150000 hasta $300000 pago con el celular
(dinero electrónico). Si es mayor a $300000 hasta $600000,
pago con la tarjeta de débito. Caso contrario, pago con la
tarjeta de crédito.
'''

#Entrada
cuenta = int(input("Ingrese la cuenta a pagar: "))

#Proceso/Salida

if cuenta < 150000:
    print("Paga en efectivo")
elif cuenta >= 150000 and cuenta <= 300000:
    print("Paga con celular")
elif cuenta >= 300000 and cuenta <= 600000:
    print("Paga con tarjeta debito")
else:
    print("Paga con tarejta de credito")