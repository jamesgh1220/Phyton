#Iniciar diccionario vacio
jugadores = {}
#Agregar elementos al diccionario
jugadores["Nombre"] = "Cristiano Ronaldo"
jugadores["Edad"] = 33
jugadores["Equipo"] = "Real Madrid"
jugadores["Pais"] = "España"
jugadores["Estado"] = "Activo"
jugadores["Posicion"] = "Delantero"

print(jugadores)

#Incrementar elementos
jugadores["Edad"] = jugadores["Edad"] + 1
print(jugadores)

#Iterar elementos
for llave, valor in jugadores.items():
    print(f'{llave}: {valor}')

#Eliminar elementos
del jugadores["Estado"]
print(jugadores)