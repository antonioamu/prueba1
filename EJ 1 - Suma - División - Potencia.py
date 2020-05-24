#Se necesita desarrollar un programa que permita calcular la suma de tres números.
# Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales),
# en caso contrario elevar el resultado al cubo.

n1 = int(input('Ingrese n1'))
n2 = int(input('ingrese n2'))
n3 = int(input('ingrese n3'))
suma = n1+n2+n3
if suma > 10:
    resultado = suma//2
else:
    resultado = suma**3
print(resultado)