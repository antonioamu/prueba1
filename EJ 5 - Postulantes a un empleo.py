# Se tienen los datos de tres postulantes a un empleo, a los que se les realizó
# un test de capacitación. Por cada postulante, se tiene entonces la siguiente
# información: nombre del postulante, cantidad total de preguntas que se le
# realizaron y cantidad de preguntas que contestó correctamente. Se pide confeccionar
# un programa que lea los datos de los tres postulantes, informe el nivel de
# cada uno según los criterios de aprobación que se indican mas abajo, e indique
# finalmente el nombre del postulante que ganó el puesto.Los criterios de aprobación
# son los siguientes, en función del porcentaje de respuestas correctas sobre el
# total de preguntas realizadas a cada postulante:
# Nivel Superior: Porcentaje 90%
# Nivel Medio: 75%6 Porcentaje < 90%
# Nivel Regular: 50%6 Porcentaje < 75%
# Fuera de Nivel: Porcentaje < 50%

postulante1 = input('Ingrese el nombre del postulante 1: ')
preguntas1 = int(input('ingrese la cantidad de preguntas realizadas: '))
respuestas1 = int(input('Ingrese la cantidad de respuestas correctas: '))
postulante2= input('ingrese el nombre del postulante 2: ')
preguntas2 = int(input('ingrese la cantidad de preg realizadas: '))
respuestas2= int(input('ingrese la cant de respuestas correctas'))
postulante3 = input('ingrese el nombre del postulante 3: ')
preguntas3 = int(input('Ingrese la cant de preg realizadas'))
respuestas3 = int(input('Ingrese la cant de respuestas correctas: '))
porcentaje1 = round((respuestas1/preguntas1*100),2)
porcentaje2 = round((respuestas2/preguntas2*100),2)
porcentaje3 = round((respuestas3/preguntas3*100),2)

if porcentaje1 >= 90:
    nivel1 = 'Nivel Superior'
elif porcentaje1 >= 75 and porcentaje1 <= 90:
    nivel1 = 'Nivel Medio'
elif porcentaje1 >= 50 and porcentaje1 <= 75:
    nivel1 = 'Nivel Regular'
elif porcentaje1 < 50:
    nivel1 = 'Fuera de Nivel'
if porcentaje2 >= 90:
    nivel2 = 'Nivel Superior'
elif porcentaje2 >= 75 and porcentaje2 <= 90:
    nivel2 = 'Nivel Medio'
elif porcentaje2 >= 50 and porcentaje2 <= 75:
    nivel2 = 'Nivel Regular'
elif porcentaje2 < 50:
    nivel2 = 'Fuera de Nivel'
if porcentaje3 >=90:
    nivel3 = 'Nivel Superior'
elif porcentaje3 >= 75 and porcentaje3 <= 90:
    nivel3 = 'Nivel Medio'
elif porcentaje3 >=50 and porcentaje3 <= 75:
    nivel3= 'Nivel Regular'
elif porcentaje3 <50:
    nivel3 = 'Fuera de Nivel'

if porcentaje1 > porcentaje2 and porcentaje2 > porcentaje3:
    ganador = postulante1
elif porcentaje2 > porcentaje3:
    ganador = postulante2
else:
    ganador = postulante3

print(postulante1, porcentaje1, nivel1)
print(postulante2, porcentaje2, nivel2)
print(postulante3, porcentaje3, nivel3)
print('El ganador es:', ganador, max(porcentaje3, porcentaje2, porcentaje1))
