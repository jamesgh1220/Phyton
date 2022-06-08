# meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
# rows = meses.__len__() # Obtenemos el tamaño del arreglo
# print(meses[11]) #Diciembre
raperos = ['Rapero 2', 'Rapero 4', 'Rapero 1', 'Rapero 3', 'Rapero 5']
print(raperos)
#ordenar elementos de la lista
raperos.sort()
print(raperos)
#Modificar elementos de la lista
raperos[0] = 'Rapero 1 modificado'
print(raperos)
#Agregar elementos de la lista
raperos.append('Rapero 6')
print(raperos)
#Eliminar elementos de la lista
del raperos[4]
print(raperos)
#Eliminar el ultimo elemento de la lista
raperos.pop()
#Eliminar una posicion de la lista
raperos.pop(0)
print(raperos)
#Eliminar por nombre
raperos.remove('Rapero 3')
print(raperos)