# Desarrollar un programa que permita al usuario jugar contra la computadora
# el clásico “Piedra, papel o tijera” y determine cuál de ellos es el ganador.
# Las reglas son:
# La piedra aplasta (o rompe) la tijera. (Gana la piedra).
# La tijera corta el papel. (Gana la tijera).
# El papel envuelve la piedra. (Gana el papel)
# Si los dos jugadores eligen el mismo elemento, empatan.


import random
jugada_usuario = input('Escriba PIEDRA, PAPEL O TIJERA para jugar')
#elementos = ('PIEDRA', 'PAPEL', 'TIJERA')
jugada_maquina = random.choice(('PIEDRA', 'PAPEL', 'TIJERA'))

if jugada_usuario == jugada_maquina:
    resultado = 'Empataron'
else:
    if (jugada_usuario == 'PIEDRA' and jugada_maquina == 'TIJERA') \
        or (jugada_usuario == 'TIJERA' and jugada_maquina == 'PAPEL') \
        or (jugada_usuario == 'PAPEL' and jugada_maquina == 'PIEDRA'):
        resultado = 'Ganó usuario'
    else:
        resultado = 'gano la maquina'

print(jugada_usuario, jugada_maquina, resultado)