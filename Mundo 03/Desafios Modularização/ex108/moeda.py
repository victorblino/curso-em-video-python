def aumentar(valor = 0, taxa = 0):
    porcento = valor * taxa / 100
    total = valor + porcento
    return total


def diminuir(valor = 0):
    porcento = valor * 10 / 100
    total = valor - porcento
    return total


def dobro(valor = 0):
    total = valor * 2
    return total


def metade(valor = 0):
    total = valor / 2
    return total

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor}'.replace('.', ',')

