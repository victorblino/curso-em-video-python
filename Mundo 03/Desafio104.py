#Exercício104

def leiaInt(n):

    valor = 0
    ok = False
    
    while True:
        n = str(input(n))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um número válido!')
        if ok:
            break
    return valor


n = leiaInt('Insira o número: ')
print(f'Você inseriu o número {n}!')