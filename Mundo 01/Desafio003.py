n1 = int(input('Insira um número para ser somado: '))
n2 = int(input('Insira outro número para ser somado ao anterior: '))

s = n1 + n2

# Antigo: print('A soma total é:', s) - Aula 04 
# Formato antigo: print('A soma total entre', n1, e, 'n2', 'é', s)
print('A soma entre {} e {} é: {}'.format(n1, n2, s))