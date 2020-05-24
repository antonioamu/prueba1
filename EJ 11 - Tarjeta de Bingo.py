# Realizar un programa que genere 15 numero aleatorios enteros en el
# rango del 1 al 100, que representaria la tarjeta de bingo de una persona.
# Una vez generado los numeros aleatorios solicitar al usuario que ingrese
# 3 numeros enteros, a partir de alli mostrar los siguientes mensajes:
# Si el usuario no marco ninguno de los numeros indicarlo diciendo “El jugador tiene mala suerte, no marco ninguna casilla”.
# Caso contrario mostrar “El jugador marco algun numero de la tarjeta”.
import random

billete = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), \
          random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), \
          random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), \
          random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), \
          random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)

primernumero = int(input('INGRESE UN NUMERO ENTERO'))
segundonumero = int(input('INGRESE UN NUMERO ENTERO'))
tercernumero = int(input('Ingrese un numero entero'))

if primernumero in billete or segundonumero in billete or tercernumero in billete:
    mensaje = 'que suerte la tuya perro'
else:
    mensaje = 'ninguna suerte gato'
print (billete, mensaje
       )