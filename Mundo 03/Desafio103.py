#Exercício103

def jogador(nome='<DESCONHECIDO>', gols = 0):
    
    """
    Programa que lê o nome de um jogador e também os gols que ele fez. 
    Caso o usuário, não informe tais opções, o programa funcionará mesmo assim com valores padrões.
    """

    print(f'O jogador {nome}, fez {gols} gols nessa temporada.')


nome = str(input('Insira o nome do jogador: '))
gols = str(input('Insira quantos gols ele fez: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    jogador(gols=gols)
else:
    jogador(nome, gols)