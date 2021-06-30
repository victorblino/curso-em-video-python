#Exercicio074

# Tabela do Campeonato Brasileiro de 2020 usada. OBS.: No lugar da Chapecoense, foi colocado o Corinthians      

tabela = ('Flamengo', 'Internacional', 'Atlético Mineiro', 'São Paulo', 'Fluminense',
            'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará SC',
            'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 
            'Goiás', 'Coritiba', 'Botafogo')

print('-'*5)
print(f'Primeiros cinco times da tabela: {tabela[:5]}')
print('-'*5)
print(f'Os quatro últimos colocados: {tabela[-5:]}')
print('-'*5)
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print('-'*5)
print(f'O Corinthians está na {tabela.index("Corinthians")}ª posição.')


