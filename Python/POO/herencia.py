#Herencia: puede crear una clase que sea hijo o una copia de otra, al heredad una clase tendra los metodos 
# y atributos de la clase padre en el hijo

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

#crear una clase hijo de restaurant

class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, nombre_hotel): #Atributos propios de la clase hijo
        super().__init__(nombre, categoria, precio) #Tomando estos atributos de la clase padre
        self.nombre_hotel = nombre_hotel