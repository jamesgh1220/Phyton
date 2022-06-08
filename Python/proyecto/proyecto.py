import os #Libreria para manejar archivos

CARPETA = 'contactos/' #constante
EXTENSION = '.txt'

class Contacto:
    def __init__(self,nombre,telefono,categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #revisa si la carpeta existe
    crear_directorio()
    #menu
    menu()
    #preguntar opcion a realizard
    preguntar = True
    while preguntar:
        opcion = input('Ingrese una opcion: \n')
        if opcion == '1':
            agregar_contacto()
            preguntar = False
        elif opcion == '2':
            editar_contacto()
            preguntar = False
        elif opcion == '3':
            ver_contactos()
            preguntar = False
        elif opcion == '4':
            buscar_contacto()
            preguntar = False
        elif opcion == '5':
            eliminar_contacto
            preguntar = False()
        else:
            print('Opcion no valida')
            preguntar = True

def crear_directorio():
    #pregunta si existe o no la carpeta y si no existe la crea
    if not os.path.exists(CARPETA):
        #crea la carpeta
        os.makedirs(CARPETA)

def menu():
    print('Seleccone una opcion:')
    print('1. Agregar contacto')
    print('2. Editar contacto')
    print('3. Ver contactos')
    print('4. Buscar contacto')
    print('5. Eliminar contacto')

def agregar_contacto():
    print('Escriba los datos el contacto:')
    nombre = input('Nombre del contacto: \n')
    #revisar si el archivo ya existe
    existe = os.path.isfile(CARPETA + nombre + EXTENSION)

    if not existe:

        with open(CARPETA + nombre + EXTENSION, 'w') as archivo:
            telefono = input('Telefono del contacto: \n')
            categoria = input('Categoria del contacto: \n')
            contacto = Contacto(nombre,telefono,categoria)

            archivo.write('Nombre: '+ contacto.nombre + '\n')
            archivo.write('Telefono: '+ contacto.telefono + '\n')
            archivo.write('Categoria: '+ contacto.categoria + '\n')

            print('\n Contacto creado exitosamente \n')
    else:
        print('El contacto ya existe')   
    #reiniciar app
    app()

def editar_contacto():
    print('Editar contacto')
def ver_contactos():
    print('Ver contactos')
def buscar_contacto():
    print('Buscar contacto')
def eliminar_contacto():
    print('Eliminar contacto')

app()