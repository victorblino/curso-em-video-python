#Exercício093

jogador = dict()
partidas = list()
somaG = 0
jogador['nome'] = str(input('Nome do jogador: '))

jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for p in range(0, jogos):
    partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na {p+1}º partida?')))
    jogador['gols'] = partidas[:]

print('-' * 20)

print(f'Jogador: {jogador["nome"]}.')

for p, g in enumerate(jogador['gols']):
    print(f'Na {p+1}º partida, {jogador["nome"]} fez {g} gols.')
    somaG += g

print(f'Total de Gols: {somaG}')

print('-' * 5)
print(f'Dicionário: {jogador}')