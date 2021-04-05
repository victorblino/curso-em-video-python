#Desafio060

'''from math import factorial

n = int(input('Insira um número para calcular teu fatorial: '))
fatorial = factorial(n)
print(f'O fatorial de {n} é {fatorial}')'''


n = int(input('Insira um número para calcular seu fatorial: '))
c = n
f = 1

print(f'Calculando {n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c-= 1 
print(f'{f}')