'''
Solicitar notas de 0.0 a 5.0 a un
estudiante y calcular promedio. Mostrar
como "Aprobo" si el promedio es mayor o
igual a 3.0, o mostrar "No aprobo" si su
nota es menor a 3.0.
'''

#Entrada

n = int(input("Ingresar nota final primer periodo: "))
n1 = int(input("Ingresar nota final segundo periodo: "))
n2 = int(input("Ingresar nota final tercer periodo: "))
#Proceso

t = n+n1+n2/5

#Salida

if t >= 3.0:
    print("El estudiante aprobo")
else:
    print("El estudiante no aprobo")
    