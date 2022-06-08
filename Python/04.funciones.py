# def hola():{
#     print("Hola")
# }

# hola()
# NO FUNCIONA print(hola())

# def suma(i,y):
#     res = i+y
#     return res 

# resultado = suma(1,2)
# print(resultado)
# def nombre(nombre):{
#     # print("Hola " + nombre)
#     print(f'Hola {nombre}')
# }

# # suma(1,2)
# nombre('James')
# nombre('otro')

def welcome():
    return 'Bienvenido'

def user(nombre):
    hola = welcome()
    print(f'{hola} {nombre}')

user('James')