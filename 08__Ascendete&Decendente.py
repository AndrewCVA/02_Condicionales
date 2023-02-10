'''
Solicitar tres números al usuario e imprimirlos en orden ascendente
y descendente.
'''

#Entrada

num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
num3 = int(input("Ingrese numero 3: "))

#Proceso/Salida

if num1 > num2:
    if num2 > num3:
        print(f"Los numero ordenados es: {num3, num2, num1}" )
    else:
        if num1 > num3:
            print(f"Los numero ordenados es: {num2, num3, num1}" )
        else:
            print(f"Los numero ordenados es: {num2, num1, num3}" )
else:
    if num1 > num3:
        print(f"Los numero ordenados es: {num3, num1, num2}" )
    else:
        if num2 > num3:
            print(f"Los numero ordenados es: {num1, num3, num2}" )
        else:
            print(f"Los numero ordenados es: {num1, num2, num3}" )