def app():

    archivo = open('archivo.txt', 'w') # w para escribir, r para leer, a para agregar
                                        #si no existe lo crea
    #generar numeros en archivo de
    for i in range(0,20):
        archivo.write(str(i) + '\n')
    
    #cerrar archivo
    archivo.close()
    


app()