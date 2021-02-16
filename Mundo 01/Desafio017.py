#Desafio017 

from math import hypot

seno = float(input('Qual é o seno? '))
coseno = float(input('Qual é o coseno? '))

print('A hipotenusa é igual a: {:.3f}'.format(hypot(seno, coseno)) )