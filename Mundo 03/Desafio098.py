#Exercício098

from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} indo de {p} em {p}:')
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
        print('- FIM -')

    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
        print('- FIM -')





contador(1, 10, 1)
contador(10, 0, 2)

contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo:')))