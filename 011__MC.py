'''
Un reporte de salud muestra una tabla diferente del índice de masa
corporal IMC de una persona que se calcula con la fórmula IMC=P/T 
en donde P es el peso en Kg. y T es la talla en metros. Lea un valor 
de P y de T, calcule el IMC y muestre su estado según 
la siguiente tabla:

IMC                  Estado

Menor a 18.5         Desnutrido
[18.5, 25)           Normal
[25,30)              Sobrepeso
[30,35)              Obesidad Grado 1
[35,40)              Obesidad Grado 2
Mayor a 40           Obesidad Grado 2
'''
 
#Entrada

Peso = int(input("Ingrese su peso en Kg: "))
Talla = float(input("Ingrese su talla en metros: "))

#Proceso

IMC = Peso / (Talla * Talla)
print(IMC)

#Salida

if IMC < 18.5:
    print("Desnutrido")

elif IMC >= 18.5 and IMC <= 24.9:
    print("Normal")
    
elif IMC >= 25 and IMC <= 29.9:
    print("Sobrepeso")
    
elif IMC >= 30 and IMC <= 34.9:
    print("Sobrepeso tipo 1")
    
elif IMC >= 35 and IMC <= 39.9:
    print("Sobrepeso tipo 2")
    
elif IMC > 40:
    print("Sobrepeso tipo 3")