# Problema  8.) Cargar por teclado dos números enteros. Mostrarlos ordenados de menor a mayor.
n1 = int(input('Ingrese un numero mayor a 0 para n1'))
n2 = int(input('Ingrese un numero mayor a 0 para n2'))
if n1 > n2:
    may = n1
    min = n2
else:
    may = n2
    min = n1
print(min, may)

# Problema  9.) Cargar por teclado tres números enteros. Determinar si el primero que se cargó es
# el mayor de los tres (informe en pantalla con un mensaje tal como: Es el mayor o No es el mayor).
n1 = int(input('ingrese n1'))
n2 = int(input('ingrese n2'))
n3 = int(input('ingrese n3'))
if n1 > n2 and n1 > n3:
    print('es el maior') #en vez de mostrar en pantalla con print, puedo guardar una variable y mostrar el print al ultimo de los bloques condicionales
else:
    print('No es el maior')
# Problema  10.) Cargar por teclado tres números enteros que se supone representan las edades de
# tres personas. Determinar si alguno de los valores cargados era negativo, en cuyo caso informe
# en pantalla con un mensaje tal como: Alguna es incorrecta:  negativa. Si todos los valores eran
# positivos o cero, informe que todas eran correctas.

edad1 = int(input('ingrese edad 1'))
edad2 = int(input('Ingrese edad 2'))
edad3 = int(input('Ingrese edad 3'))

if edad1<0 or edad2<0 or edad3 < 0:
    mensaje= 'Alguna es incorrenta: negativa'
else:
    mensaje = 'Todas correctas'
print(mensaje
      )


n = int(input('ingrese un numero entero'))

if n:
    print('no es cero')
else:
    print('es cero')

cad = 'gilas'
if cad:
    print(cad)
else:
    print('la cadena esta vacia')