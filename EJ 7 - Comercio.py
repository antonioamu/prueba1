# Un comerciante tiene a la venta 3 tipos de articulos principales.
# Conociendo la cantidad vendida de cada articulo y el precio unitario
# de cada articulo, hacer un programa que determine cuál fue el producto
# que realizó el mayor aporte en los ingresos y el porcentaje que dicho
# aporte significa en el ingreso absoluto de los 3 articulos sumados.
# Ese porcentaje se calcula así:


name_article_1 = input('ingrese el nombre del articulo')
quantity_1 = int(input('Ingrese la cantidad de articulos'))
price_1 = float(input('Ingrese el precio del articulo'))

name_article_2 = input('Ingrese el nombre del articulo')
quantity_2 = int(input('Ingrese la cantidad de articulos'))
price_2 = float(input('Ingrese el precio del articulo'))

name_article_3 = input('Ingrese el nombre del articulo')
quantity_3 = int(input('Ingrese el nombre del articulo'))
price_3 = float(input('Ingrese el precio del articulo'))

total1 = quantity_1*price_1
total2 = quantity_2*price_2
total3 = quantity_3*price_3

if total1 > total2 and total1 > total3:
    mayor = name_article_1, total1
    porcentaje = total1*100/(total1+total2+total3)
elif total2 > total1 and total2 > total3:
    mayor = name_article_2, total2
    porcentaje = total2*100/(total1+total2+total3)
else:
    mayor = name_article_3, total3
    porcentaje = total3*100/(total1+total2+total3)

print(mayor, porcentaje
      )