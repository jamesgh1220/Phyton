#Encapsulamiento: permite restrunguir u ocultar el acceso a los datos dentro de la misma clase

class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Default: Public
        self._categoria = categoria #PROTECTED: puede ser modificado dentro de la misma clase
        self.__precio = precio #PRIVATE
    
    def mostrar_informacion(self):
        print(f'El restaurante {self.nombre} esta abierto, Categoria: {self._categoria},  Precio: {self.__precio}')

    #GETTERS Y SETTERS -> GET: obtiene un valor, SET: agrega un valor,
    def get_precio(self):
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio

restaurant = Restaurant('La casa de papá', 'Comida china', 50)

# restaurant.__precio = 67 #No es posible modificarlo por ser PRIVATE
restaurant.mostrar_informacion()
restaurant.set_precio(77)
restaurant.get_precio()

restaurant2 = Restaurant('La casa de la esquina', 'Comida italiana', 90)

restaurant2.mostrar_informacion()
restaurant2.set_precio(33)
restaurant2.get_precio()
