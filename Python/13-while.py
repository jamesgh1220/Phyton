preguntar = True

while preguntar:
    numero = input('Ingresa un numero para saber si es par: \r\nEscribir "salir" para salir: \r\n')
    if numero == 'salir':
        preguntar = False
    else:
        numero = int(numero)
        if numero % 2 == 0:
            print('El numero es par')
        else:
            print('El numero es impar')