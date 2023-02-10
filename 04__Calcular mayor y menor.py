'''
Solicitar dos números al usuario y calcular cuál es el mayor y 
cuál es el menor.
'''

#Entrada

n = int(input("Ingrese su primer número: "))
n1 = int(input("Ingrse su segundo número: "))

#Proceso/Salida

if n > n1:
    print(n, "es mayor a" ,n1)
else:
    print(n, "es menor a" ,n1)
    