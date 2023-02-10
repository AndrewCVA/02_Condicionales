'''
Solicitar un número al usuario y determinar si es par, impar o cero.
'''

#Entrada

n = int(input("Ingrese un número: "))

#Proceso/Salida

if n == 0:
    print (n, "es cero")
elif n % 2 == 0:
    print (n, "es par")
else:
   print (n, "es impar")
