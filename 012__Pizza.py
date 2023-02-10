'''
El precio que debe pagar un cliente por una pizza depende del 
tamaño seleccionado, como se muestra a continuación:

Precio             Tamaño
$15.000               1
$24.000               2
$36.000               3

Si cada ingrediente adicional cuesta $4.000.
Escribir un programa que solicite al empleado encargado de registrar 
las ventas, el tamaño de la pizza y el número de ingredientes 
adicionales y muestre al cliente el precio que debe pagar.
'''

#Entrada

menu = """  
   Precio     Tamaño
    
1. $15.000    Pequeña
2. $24.000    Mediana
3. $36.000    Grande

Seleccione tamaño de pizza:
"""
venta = int(input("Numero de venta: "))
opcion = int(input(menu))

#Proces/Salida

if opcion == 1:
    ingredientesAdi = int(input("Cuantos ingrendientes adicionales quiere: "))
    total = (ingredientesAdi * 4000) + 15000
    print(f"Venta: #{venta}")
    print("Tamaño: Pequeño")
    print(f"Total: ${total}")
    
elif opcion == 2:
    ingredientesAdi = int(input("Cuantos ingrendientes adicionales quiere: "))
    total = (ingredientesAdi * 4000) + 24000
    print(f"Venta: #{venta}")
    print("Tamaño: Pequeño")
    print(f"Total: ${total}")
    
elif opcion == 3:
    ingredientesAdi = int(input("Cuantos ingrendientes adicionales quiere: "))
    total = (ingredientesAdi * 4000) + 25000
    print(f"Venta: #{venta}")
    print("Tamaño: Pequeño")
    print(f"Total: ${total}")
else:
    print("Ingrese una opcion valida")