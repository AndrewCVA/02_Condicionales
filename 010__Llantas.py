'''
Leer el número de llantas de una compra y mostrar el valor 
que debe pagarse. 
El almacén las vende con la siguiente política: Si se 
compran menos de 6 llantas,
el precio unitario es $240000. Si se compran 6 o 7, 
el precio unitario es $221000,
y si se compran más de 7 llantas, el precio unitario es $180000.
'''

#Entrada

Llantas = int(input("Ingrese el número de llantas que va a llevar: "))

#Proceso/Salida

if Llantas < 6:
    unitprecio = 240000 * Llantas
    print(f"El total a pagar es de: {unitprecio}")

elif Llantas == 6 | Llantas == 7:
    unitprecio = 221000 * Llantas
    print(f"El total a pagar es de: {unitprecio}")
    
elif Llantas > 7:
    unitprecio = 180000 * Llantas
    print(f"El total a pagar es de: {unitprecio}")