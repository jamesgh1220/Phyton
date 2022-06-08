def app():

    with open('archivo.txt') as archivo:
        for linea in archivo:
            print(linea)

app()