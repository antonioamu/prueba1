# Se necesita desarrollar un programa para el área de recursos humanos
# de una empresa que permita informar el jornal de un determinado operario.
# Usted deberá cargar por teclado el código de turno que el operario trabajó
# ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas
# trabajadas. La política de trabajo en la empresa es que los operarios de la
# misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja
# en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno
# diurno cobra 35.50 pesos la hora.

turno = input('Ingrese el código de turno D/N')
if turno == 'D':
    pago = 35.50
else:
    pago = 40.60
horas = int(input('Ingrese la cantidad de horas trabajadas'))
jornal = horas*pago
print(turno, pago, jornal)