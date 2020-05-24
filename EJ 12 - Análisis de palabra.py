# Se pide un programa que le solicite al usuario que ingrese una palabra.
# Con esa palabra calcular los siguientes puntos:
# Determinar la cantidad de letras que ene la palabra
# Mostrar un mensaje que informe si la palabra termina en vocal

palabra = input('Ingrese una palabra:')
total_letras = len(palabra)
#ultimo_digito = total_letras-1
ultima_letra = palabra[total_letras-1]


if ultima_letra == 'a' or ultima_letra == 'e' or ultima_letra == 'i' or ultima_letra == 'o' or ultima_letra =='u':
    print('La palabra termina en vocal')
print('palabra:', palabra, 'total de letras', total_letras, 'ultimaletra:', ultima_letra)