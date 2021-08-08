#Exercício102

def fatorial(n, show=False):

    """
    -> Calcula o fatorial, sendo opcional a opção de mostrar a conta.
        Feito por ADMVicli para o Curso de Python do Curso em Vídeo.
    """
    f = 1 
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ',end='')
        f *= c
    return f

print(fatorial(3, show = True))