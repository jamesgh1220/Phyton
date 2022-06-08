class Restaurant:
    
    def agregar_restaurant(self,nombre):
        self.nombre = nombre
    
    def mostrar_informacion(self):
        print(f'El restaurante {self.nombre} esta abierto')

restaurant = Restaurant()
restaurant.agregar_restaurant('La casa de papa')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('La casa de la esquina')
restaurant2.mostrar_informacion()

print(f'Nombre restaurante: {restaurant.nombre}')
print(f'Nombre restaurante: {restaurant2.nombre}')