# habilidad de tener diferentes comportamientos basado en que una sublase se esta
# utilizando, relacionado muy estrechamente con herencia

class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Default: Public
        self._categoria = categoria #PROTECTED: puede ser modificado dentro de la misma clase
        self.precio = precio #PRIVATE
    
    def mostrar_informacion(self):
        print(f'El restaurante {self.nombre} esta abierto, Categoria: {self._categoria},  Precio: {self.precio}')

    #GETTERS Y SETTERS -> GET: obtiene un valor, SET: agrega un valor,
    def get_precio(self):
        print(self.precio)

    def set_precio(self, precio):
        self.precio = precio

#crear una clase hijo de restaurant

class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, nombre_hotel): #Atributos propios de la clase hijo
        super().__init__(nombre, categoria, precio) #Tomando estos atributos de la clase padre
        self.nombre_hotel = nombre_hotel #especifico de la clase hotel

    def mostrar_informacion(self):
        print(f'El restaurante {self.nombre} esta abierto, Categoria: {self._categoria}, Precio: {self.precio}, Hotel: {self.nombre_hotel}')

    #metodo que solo exista en Hotel
    def getNombreHotel(self):
        print(self.nombre_hotel)

hotel = Hotel('Restaurante Toño', '5 estrellas', '$500', 'Hotel Marriot')
hotel.mostrar_informacion()
hotel.getNombreHotel()