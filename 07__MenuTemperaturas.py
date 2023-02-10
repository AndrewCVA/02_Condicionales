'''
Conversión de temperaturas. Crear un menú de opciones.
'''

#Entrada

menu = """Conversión de temperaturas.

1 - °|Fahrenheit a Celcius|°
2 - °|Fahrenheit a Kelvin|°
3 - °|Fahrenheit a Rankine|°
4 - °|Farenheit a Réaumur|°
5 - °|Celcius a Fahrenheit|°
6 - °|Celcius a Kelvin|°
7 - °|Celcius a Rankine|°
8 - °|Celcius a Réaumur|°
9 - °|Kelvin a Celcius|° 
10 - °|Kelvin a Fahrenheit|°
11 - °|Kelvin a Rankine|°
12 - °|Kelvin a Réaumur|°
13 - °|Rankine a Celcius|°
14 - °|Rankine a Fahrenheit|°
15 - °|Rankine a Kelvin|°
16 - °|Rankine a Réaumur|°
17 - °|Réaumur a Celcius|°
18 - °|Réaumur a Fahrenhite|°
19 - °|Réaumur a Kelvin|°
20 - °|Réaumur a Rankine|°

Seleccione la temperatura a que desea convertir:

"""

opcion = int(input(menu))

#Proceso/Salida

if opcion == 1:
    print("°|Fahrenheit a Celcius|°")

    Fahrenheit = int(input("Ingrese los grados farenheit: "))

    Celcius = (Fahrenheit - 32)/1.8

    print(f"Convertido a grados celcius es: {Celcius}")

elif opcion ==2:
    print("°|Fahrenheit a Kelvin|°")

    Fahrenheit = int(input("Ingrese los grados farenheit: "))

    Kelvin =(Fahrenheit+459.67)/1.8

    print(f"Convertido a grados kelvin es: {Kelvin}")

elif opcion == 3:
    print("°|Fahrenheit a Rankine|°")

    Fahrenheit = int(input("Ingrese los grados farenheit: "))

    Rankine =  Fahrenheit+459.67

    print(f"Convertido a grados rankine es: {Rankine}")

elif opcion == 4:
    print("°|Farenheit a Réaumur|°")

    Fahrenheit = int(input("Ingresar los grados farenheit: "))

    Réaumur = (Fahrenheit-32)/2.25

    print(f"Convertido a grados réaumur es: {Réaumur}")

elif opcion == 5:
    print("°|Celcius a Fahrenheit|°")

    Celcius = int(input("Ingresar los grados celcius: "))

    Fahrenheit = Celcius*1.8+32

    print(f"Convertido a grados fahrenheit es: {Fahrenheit}")

elif opcion == 6:
    print("°|Celcius a Kelvin|°")

    Celcius = int(input("Ingresar los grados celcius: "))

    Kelvin = Celcius+273.15

    print(f"Convertido a grados kelvin es: {Celcius}")

elif opcion == 7:
    print("°|Celcius a Rankine|°")

    Celcius = int(input("Ingrese los grados celcius: "))

    Rankine = Celcius*1.8+32+459.67

    print(f"Convertido a grado  rankine es: {Rankine}")

elif opcion == 8:
    print("°|Celcius a Réaumur|°")

    Celcius = int(input("Ingrese los grados celcius: "))

    Réaumur = Celcius*0.8

    print(f"Convertido a grados réaumur: {Réaumur}")

elif opcion == 9:
    print("°|Kelvin a Celcius|°")

    Kelvin = int(input("Ingrese los grados kelvin: "))

    Celcius = Kelvin-273.15

    print(f"Convertido a grados celcius es: {Celcius}")

elif opcion == 10:
    print(" °|Kelvin a Fahrenheit|°")

    Kelvin = int(input("Ingrese los grados kelvin: "))

    Fahrenheit = Kelvin*1.8-459.67

    print(f"Convertido a grados fahrenheit es: {Fahrenheit}")

elif opcion == 11:
    print("°|Kelvin a Rankine|°")

    Kelvin = int(input("Ingrese los grados kelvin: "))

    Rankine = Kelvin*1.8

    print(f"Convertido a grados rankine es: {Rankine}")

elif opcion == 12:
    print("°|Kelvin a Réaumur|°")

    Kelvin = int(input("Ingrese los grados kelvin: "))

    Réaumur = (Kelvin-273.15)*0.8

    print(f"Convertido a grados réaumur es: {Réaumur}")

elif opcion == 13:
    print("°|Rankine a Celcius|°")

    Rankine = int(input("Ingresar los grados rankine: "))

    Celcius = (Rankine-32-359-67)/1.8

    print(f"Convertido a grados celcius es: {Celcius}")

elif opcion == 14:
    print("°|Rankine a Fahrenheit|°")

    Rankine = int(input("Ingresar los grados rankine: "))

    Fahrenheit = Rankine-459.67

    print(f"Conertido a grados fahrenheit es: ")

elif opcion == 15:
    print("°|Rankine a Kelvin|°")

    Rankine = int(input("Ingrese los grados rankine: "))

    Kelvin = Rankine/1.8

    print(f"Convertido a grados kelvin es: {Kelvin}")

elif opcion == 16:
    print("°|Rankine a Réaumur|°")

    Rankine = int(input("Ingrese los grados rankine: "))

    Réaumur = (Rankine-32-459.67)/2.25

    print(f"Convertido a grados réaumur es: {Réaumur}")

elif opcion == 17:
    print("°|Réaumur a Celcius|°")
    
    Réaumur = int(input("Ingresar los grados réamur: "))

    Celcius = Réaumur*1.25

    print(f"Convertido a grados celcius: {Celcius}")

elif opcion == 18:
    print("°|Réaumur a Fahrenhite|°")

    Réaumur = int(input("Ingresar los grados réamur: "))

    Fahrenheit = Réaumur*2.25+32

    print(f"Convertido a grados fahrenheit es: {Fahrenheit}")

elif opcion == 19:
    print("°|Réaumur a Kelvin|°")

    Réaumur = int(input("Ingresar los grados réaumur: "))
    
    Kelvin = Réaumur*1.25+273.15

    print(f"Convertido a grados kelvin es: {Kelvin}")

elif opcion == 20:
    print("°|Réaumur a Rankine|°")

    Réaumur = int(input("Ingresar los grados réaumur: "))

    Rankine = Réaumur*2.25+32+459.67

    print(f"Convertido a grados rankine es: {Rankine}")
     