# nombre = input('Cual es tu nombre: \r\n')

# print(f'Hola {nombre}')

#leer datos numericos
edad = input('Cual es tu edad: \r\n')
#convertir a entero
edad = int(edad)
if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

#mezcla de datos con operadores logicos
numero = input('Ingresa un numero y si es par o no: \r\n')
if numero % 2 == 0:
    print('Es par')