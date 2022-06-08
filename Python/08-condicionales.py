#== Igual a
#!= Diferente a
#> Mayor que
#< Menor que
#>= Mayor o igual que
#<= Menor o igual que

edad = 27

if edad > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#If aninadados

autenticado = False
admin = False

if autenticado:
    if admin:
        print("Bienvenido al sistema")
    else:
        print("Bienvenido")
else:
    print("No autenticado")