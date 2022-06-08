canciones = {
    'title': 'La vida es bella', #Llave y valor
    'artist': 'Shakira',
    'album': 'Viva la vida',
    'year': 1997,
}

print(canciones)
#Acceder a los valores
print(canciones['title'])

year = canciones['year']
print(f'Se lanzo en el año: {year}')

#Agrego un nuevo valor
canciones['duration'] = 4.5
print(canciones)

#Reescribir un valor
canciones['year'] = 2018
print(canciones)

#Eliminar un valor
del canciones['duration']
print(canciones)