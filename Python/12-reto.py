# Realizar 3 preguntas al usuario , el usuario debera responder si o no
# y al final entregarle una calificacion de 0 a 3

respuesta1 = 24
respuesta2 = 'Bogota'
respuesta3 = 14
calificacion = 0

pregunta1 = input('Cuanto es 4!: \r\n')
pregunta1 = int(pregunta1)

if pregunta1 == respuesta1:
    calificacion+=1

pregunta2 = input('Cual es la capital de Colombia: \r\n')
pregunta2 = pregunta2.lower()
if pregunta2 == respuesta2.lower():
    calificacion+=1

pregunta3 = input('Cuantas Champions League tiene el Real Madrid: \r\n')
pregunta3 = int(pregunta3)
if pregunta3 == respuesta3:
    calificacion+=1

print(f'Tu calificacion es: {calificacion}')