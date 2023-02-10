'''
Preguntar al usuario el nombre y la edad,
si es mayor o igual a 18 años mostrar el
mensaje "Usted es mayor de edad", de lo
contrario "Usted es menor de edad". Si el
número ingresado es negativo o la edad
ingresada es mayor de 100 años, mostrar
al usuario un mensaje de ingresar una
edad válida.
'''

#Entrada

name = input("Ingrese su nombre: ")
n = int (input("Ingrese su edad: "))

#Proceso

if n >= 18 and n <= 99:
    print (name, "Usted es mayor de edad")
elif n >= 1 and n <= 18:
    print (name, "Usted es menor de edad")
elif n >= 100:
    print ("Introduzca una edad válida")
elif n <= 0:
    print ("Introduzca una edad válida")
