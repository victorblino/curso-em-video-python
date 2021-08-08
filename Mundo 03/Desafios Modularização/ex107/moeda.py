def aumentar(valor, taxa):
    porcento = valor * taxa / 100
    total = valor + porcento
    return total


def diminuir(valor):
    porcento = valor * 10 / 100
    total = valor - porcento
    return total


def dobro(valor):
    total = valor * 2
    return total


def metade(valor):
    total = valor / 2
    return total