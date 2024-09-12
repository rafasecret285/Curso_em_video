import math

angulo = float(input('Digite um ângulo:'))
radiante = math.radians(angulo)

seno = math.sin(radiante)
coseno = math.cos(radiante)
tangente = math.tan(radiante)

print('O seno do ângulo é {:.2f}^,\nSeu conseno é {:.2f},\nE sua tangente {:.2f}'.format(seno,coseno,tangente))

