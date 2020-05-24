# Realice un programa que le permita calcular el Índice de Masa Corporal (IMC)
# de una persona en función de su peso (en Kg.) y su altura (en mts.), sabiendo
# que el IMC es igual al peso dividido la altura al cuadrado. En función del valor
# del IMC, el programa debe mostrar por pantalla el diagnósco resultante del
# análisis del índice según las siguientes situaciones:
#
# Si el IMC es menor o igual a 16: “Necesita asistencia
# de un médico, los riesgos para su salud son muy altos”.
# # Si el IMC es menor o igual a 17: “Usted ene infrapeso, aliméntese más”.
# # Si el IMC es menor o igual a 18: “Usted ene bajo peso, aliméntese mejor”.
# Si el IMC es mayor a 18 y menor o igual a 26: “Usted ene un peso saludable, connúe así!”.
# Si el IMC es mayor a 26 y menor a 30: “Tiene sobrepeso de grado I, hoy es
# un buen día para empezar a hacer ejercicios”.
# Si el IMC es mayor o igual a 30 y menor o igual a 35: “Tiene obesidad de
# grado II, necesita el apoyo de un plan nutricional”.
# Si el IMC es mayor a 35 y menor o igual a 40: “Tiene obesidad grado III
# (pre-mórbida), consulte con su médico los riesgos para su salud”.
# Si el IMC es mayor a 40: “Usted tiene obesidad de grado IV (mórbida),
# los riesgos para su salud son muy altos, consulte con su médico a la brevedad”.

peso = float(input('Ingrese su peso en kg'))
altura = float(input('Ingrese su altura en mts'))
IMC = round((peso/altura**2),2)

if IMC <= 16:
    mensaje = '“Necesita asistencia de un médico, los riesgos para su salud son muy altos”'
elif IMC <= 17:
    mensaje = '“Usted tiene infrapeso, aliméntese más”'
elif IMC <= 18:
    mensaje = '“Usted tiene bajo peso, aliméntese mejor”'
elif IMC > 18 and IMC <= 26:
    mensaje = '“Usted tiene un peso saludable, continúe así!”'
elif IMC > 26 and IMC <= 30:
    mensaje= '“Tiene sobrepeso de grado I, hoy es un buen día para empezar a hacer ejercicios”'
elif IMC >= 30 and IMC <= 35:
    mensaje = '“Tiene obesidad de grado II, necesita el apoyo de un plan nutricional”'
elif IMC > 35 and IMC <= 40:
    mensaje = '“Tiene obesidad grado III (pre-mórbida), consulte con su médico los riesgos para su salud”'
elif IMC > 40:
    mensaje = '“Usted tiene obesidad de grado IV (mórbida), los riesgos para su salud son muy altos, consulte con su médico a la brevedad”'

print(altura, peso, IMC, mensaje)