# Se solicita realizar un programa que permita generar tres temperaturas
# en forma aleatoria (correspondientes a diferentes momentos de un día) y determinar:
# Cual es el promedio de las temperaturas
# Si existe alguna temperatura que sea mayor al promedio
import random
temperatura1 = round(random.uniform(20.5, 36.7),2)
temperatura2 = round(random.uniform(10.3, 28.6),2)
temperatura3 = round(random.uniform(7.9, 20.6),2)

promedio = round((temperatura1+temperatura2+temperatura3) / 3, 2)

if temperatura1 > promedio: #if temperatura1 > promedio or temperatura2 > promedio or temperatura3 > promedio: votra manera de haerlo pero sin saber cual temp supera
    print('La temp 1 es mayor que el promedio', temperatura1)
if temperatura2 > promedio:
    print('la temp 2 es mayor que el promedio', temperatura2)
else:
    print('la temp 3 es mayor que el promedio', temperatura3)

print('temp1:', temperatura1, '\n'
      'temp2:', temperatura2, '\n'
      'temp3:', temperatura3, '\n'
      'promedio:', promedio)