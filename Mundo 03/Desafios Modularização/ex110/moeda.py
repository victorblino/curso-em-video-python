def aumentar(valor = 0, taxa = 0, format=False):

    """
    Aumenta um valor que o usuário pode escolher, sendo o padrão de 10%.
    """

    porcento = valor * taxa / 100
    total = valor + porcento
    return total if format is False else moeda(total)


def diminuir(valor = 0, taxa = 0, format=False):

    """
    Diminui um valor que o usuário pode escolher, sendo o padrão de 10%
    """
    porcento = valor * taxa / 100
    total = valor - porcento
    return total if format is False else moeda(total)


def dobro(valor = 0, format=False):

    """
    Dobra inserido pelo o usuário.
    """

    total = valor * 2
    return total if format is False else moeda(total)


def metade(valor = 0, format=False):

    """
    Pega a metade de um valor, escolhido por um usuário.
    """

    total = valor / 2
    return total if format is False else moeda(total)

def moeda(valor = 0, moeda = 'R$'):
    """
    Formata o valor para que o "." seja trocado por ",".
    """

    return f'{moeda}{valor}'.replace('.', ',')

def resumo(valor, taxaAumento, taxaDiminuir):
    print(f'Valor inserido: {moeda(valor)}')
    print(f'O dobro do valor: {dobro(valor, True)}')
    print(f'Metade do valor: {metade(valor, True)}')
    print(f'Taxa de {taxaAumento}% de aumento: {aumentar(valor, taxaAumento, True)}')
    print(f'Taxa de {taxaDiminuir}% de diminuição%: {diminuir(valor, taxaDiminuir, True)}')