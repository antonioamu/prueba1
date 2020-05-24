# Una galería de arte desea preparar un catálogo de sus cuadros más famosos.
# Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en
# que fue creado. El programa deberá verificar si todos los cuadros son anteriores
# al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó
# en el año 2000). Determinar cuántos tienen antigüedad inferior a 10 años. Si no
# hay ninguno, imprimir el mensaje “Renovar stock”.

añocuadrouno = int(input('Ingrese el año del primer cuadro'))
añocuadrodos = int(input('Ingrese el año del segundo cuadro'))
añocuadrotres = int(input('Ingrese el año del tercer cuadro'))
añoactual = 2020

son_antiguas = añocuadrouno < 1901 and añocuadrodos < 1901 and añocuadrotres < 1901

if añoactual-añocuadrouno > 10 and añoactual-añocuadrodos > 10 and añoactual-añocuadrotres > 10:
    print('renovar stock')
if son_antiguas==True:
    print('Todas las obras son anteriores al siglo XX')
else:
    print('caca')