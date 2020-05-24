# Crear un programa que permita calcular los impuestos que debe pagar un auto,
# conociendo su modelo (año de fabricación) y tipo (P: Parcular/T: Taxi/R: Remis).
# Para calcular los impuestos, tener en cuenta que:
 #Los autos parculares de menos de 10 años de angüedad pagan $200, entre 10 y 20
# años pagan $150 y no pagan impuestos los que enen más de 20 años.
# Los taxis pagan impuestos como auto parcular, más $150 por la licencia de taxi.
# Los remises pagan $100 por cada año de angüedad de su vehículo

modelo = int(input('Ingrese el año del vehiculo'))
tipo = input('Ingrese el tipo (particular, taxi, remis P/T/R')
antiguedad = 2020-modelo

if tipo == 'P' or tipo == 'T':
    if antiguedad < 10:
        impuesto = 200
    elif antiguedad>10 and antiguedad < 20:
        impuesto = 150
    else:
        impuesto = 0
    if tipo == 'T':
        impuesto = impuesto+150
else:
    impuesto = antiguedad*100

print(impuesto)