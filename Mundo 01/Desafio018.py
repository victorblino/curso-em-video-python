#Desafio018

from math import sin, cos, tan,radians

n = float(input('Insira um ângulo: '))

s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))

print('O ângulo {} tem como seno: {:.3f}, coseno: {:.3f} e tangente: {:.3f}'.format(n, s, c, t))    