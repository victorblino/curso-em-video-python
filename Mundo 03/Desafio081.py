#Exercício081

lista = []

while True:
    lista.append(int(input('Insira um valor: ')))

    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break

lista.sort(reverse=True)

print(f'Foi digitado {len(lista)} valores.')
print(f'A lista de valores em ordem decrescente: {lista}')

if 5 in lista:
    if lista.count(5) == 1:
        print(f'O número 5 faz parte da lista e foi encontrado {lista.count(5)} vez.')
    else:
        print(f'O número 5 faz parte da lista e foi encontrado {lista.count(5)} vezes.')
# Aqui eu coloquei isso porque eu só quis, não é nescessário (porque o exercício não pede mas eu coloquei DHUASDASDA foda.)
else:
    print('O número 5 não foi digitado.')


