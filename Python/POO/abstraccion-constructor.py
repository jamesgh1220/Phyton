class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    
    def mostrar_informacion(self):
        print(f'El restaurante {self.nombre} esta abierto, Categoria: {self.categoria},  Precio: {self.precio}')

restaurant = Restaurant('La casa de papá', 'Comida china', 50)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('La casa de la esquina', 'Comida italiana', 90)
restaurant2.mostrar_informacion()