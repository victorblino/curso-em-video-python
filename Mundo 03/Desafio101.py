#Exercício101


def voto(idade):
    
    """
    Função para descobrir se uma pessoa pode votar com a idade de acordo com o ano de nascimento.

    Idade: É calculado o ano que vocês nasceu menos o ano atual.
    """

    from datetime import datetime

    atual = datetime.now().year - idade

    if atual < 16:
        print(f'Com {atual} anos, o voto é NEGADO.')
    elif atual <= 16 or atual < 18 or atual > 70:
        print(f'Com {atual} anos, o voto é OPCIONAL.')
    else:
        print(f'Com {atual} anos, o voto é OBRIGATÓRIO.')

idade = int(input('Insira o ano de nascimento: ')) 

voto(idade)