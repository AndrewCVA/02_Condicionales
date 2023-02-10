'''
Crear un programa con un menú de
opciones, que permita calcular las áreas
de figuras geométricas (cuadrado,
rectángulo, triángulo, círculo, rombo y
trapecio).
'''

#Entrada

Pi = 3.14159

menu = """Seleccione el área a calcular:
1 - Cuadrado
2 - Rectángulo
3 - Triángulo
4 - Círculo
5 - Rombo
6 - Trapecio

Seleccione el área que quiere calcular:
"""

opcion = int(input(menu))

#Proceso/Salida

if opcion == 1:
    lado = int(input("Ingrese el lado:"))

    totalcuadrado = lado*lado

    print(f"El área del cuadrado es: {totalcuadrado}")

elif opcion == 2:
    largo = int(input("Ingrese el largo: "))
    ancho = int(input("Ingrese el ancho: "))

    totalrectangulo = largo*ancho

    print(f"El área del rectángulo es: {totalrectangulo}")

elif opcion == 3:
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))

    totaltriangulo = base*altura/2

    print(f"El área del triángulo es: {totaltriangulo}")

elif opcion == 4:
    radio = int(input("Ingrese el radio: "))

    totalcirculo = Pi*radio**2

    print(f"El área del círculo es: {totalcirculo}")

elif opcion == 5:
    diagmay = int(input("Ingrese la diagonal mayor: "))
    diagmen = int(input("Ingrese la diagonal menor: "))

    totalrombo = diagmay*diagmen/2

    print(f"El área del rombo es: {totalrombo}")

elif opcion == 6:
    basemay = int(input("Ingrese base mayor: "))
    basemen = int(input("Ingrese base menor: "))
    altura = int(input("Ingresar altura: "))

    totaltrapecio = basemay+basemen*altura/2

    print(f"El área del trapecio es: {totaltrapecio}")
    