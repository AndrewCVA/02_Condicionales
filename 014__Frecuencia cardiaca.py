'''
El número de pulsaciones que debe tener una persona por cada 10 segundos 
de ejercicio aeróbico se calcula con la fórmula:
    
    Género femenino (1): número de pulsaciones = (220 - edad en años)/10
    
    Género masculino (2): número de pulsaciones = (210 - edad en años)/10
    
    Lea la edad y el género y muestre el número de pulsaciones.
'''

#Entrada

name = input("Cual es su nombre: ")
genero = """Cual es su genero: 
1 - Masculino
2 - Femenino 
"""
edad = int(input("Ingrese edad: "))
frcar = int(input("Ingrese cantidad de pulsaciones: ")) 

opcion = int(input(genero))

#Proceso/Salida

if opcion == 1:
    frcar = (220 -  edad)/10
    print(f"Nombre: {name}")
    print("Genero: Masculino")
    print(f"Edad: {edad}")
    print(f"Pulsaciones: {frcar}")

elif opcion == 2:
    frcar = (210 -  edad)/10
    print(f"Nombre: {name}")
    print("Genero: Femenino")
    print(f"Edad: {edad}")
    print(f"Pulsaciones: {frcar}")
else:
    print("Seleccione un genero valido.")