'''
Solicitar un número al usuario y determinar si es negativo, 
positivo o cero.
'''

#Entrada

n = int(input("Inserte el número: "))

#Proceso/Salida

if n == 0: 
    print ("Es cero")
elif n <= -1:
    print ("Es negativo")
elif n >= 1:
    print ("Es positivo")
    