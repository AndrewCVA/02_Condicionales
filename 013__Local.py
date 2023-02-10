'''
Un local vende sus productos con la siguiente promoción. 
Si compra hasta 5 artículos, no hay descuento. 
Si compra más de 5 artículos,
pero menos de 10, el precio unitario se reduce en 5%. 
Si compra 10 o más artículos,
el precio unitario se reduce en 8%. Ingrese un dato de 
cantidad y el valor del precio unitario original. 
Calcule y muestre el valor total a pagar.
'''

#Entrada

cantidad = int(input("Ingrese cantidad a llevar: "))
valorUnitario = float(input("Ingrese el valor unitario: "))

#Proceso/Salida

if cantidad <= 5:
    total = valorUnitario * cantidad
    print(f"No obtiene descuento, el valor total es: {total}")
elif cantidad < 10:
    descuento = valorUnitario * 0.5
    total = (valorUnitario - descuento) * cantidad
    print(f"Obtiene descuento unitario del 5%, el valor total seria: {total}")
else:
    descuento = valorUnitario * 0.8
    total = (valorUnitario - descuento) * cantidad
    print(f"0btiene descuento unitario del 8%, el valor total seria: {total}")