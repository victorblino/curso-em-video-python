#Exercício092

from datetime import datetime

dados = dict()

dados['Nome'] =  str(input('Insira o seu nome: '))
ano = int(input('Insira o ano que você nasceu: '))
dados['Idade'] = datetime.now().year - ano
dados['Carteira de Trabalho'] = int(input('Insira a carteira de trabalho (0 caso não tenha): '))


if dados['Carteira de Trabalho'] != 0:
    dados['Contratacão'] = int(input('Insira o ano da contratação: '))
    dados['Salário'] = float(input('Insira o salário: '))
    dados['Aposentadoria'] = dados['Idade'] + 35

for k, i in dados.items():
    print(f'{k}: {i}')