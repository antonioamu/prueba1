# La facultad pide un simple programa que pida las tres notas de un alumno en
# cualquier materia y mostrar si el alumno esta libre, regular o promocionado.
# Las tres notas son los dos parciales mas la nota de práccos y las condiciones
# de regularidad están descriptas a connuación:
# El promedio menor a 4 el alumno esta libre
# El promedio comprendido entre 4 y 8 el alumno esta regular
# El promedio mayor a 8 el alumno está promocionado.


parcial1 = int(input('Ingrese la nota del parcial 1'))
parcial2 = int(input('Ingrese la nota del parcial 2'))
practicos = int(input('Ingrese la nota de los practicos'))
promedio = (parcial1+parcial2+practicos) / 3

if promedio < 4:
    alumno = 'alumno libre'
elif promedio >= 4 and promedio <= 8:
    alumno = 'alumno regular'
else:
    alumno = 'alumno promocional'
print(round(promedio,2), alumno)