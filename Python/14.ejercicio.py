# playlist ={}
# playlist['canciones'] = []
playlist = {
    'canciones': []
}

#funcion ppal
def app():
    #Agregar canciones
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input("Ingrese el nombre de la playlist: \n")
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            #Desactivar nombre playlist
            agregar_playlist = False
            #invocar Funcion agregar canciones
            agregar_canciones()

#Agregar canciones
def agregar_canciones():
    agregar_cancion = True
    nombre_playlist = playlist['nombre']
    while agregar_cancion:
        cancion = input(f'Ingrese el nombre de la cancion para la playlist {nombre_playlist}: \nEscribe "x" para dejar de agregar canciones\n')
        if cancion == 'x':
            agregar_cancion = False
            #mostrar resumen de la playlist
            mostrar_playlist()
        else:
            playlist['canciones'].append(cancion)

#mostrar canciones
def mostrar_playlist():
    nombre_playlist = playlist['nombre']
    canciones = playlist['canciones']
    print(f'Playlist: {nombre_playlist}')
    print(f'Canciones: {canciones}')



app()