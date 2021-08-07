#Exercício090

aluno = dict()

aluno['nome'] = str(input('Insira o nome do aluno: '))
aluno['media'] = float(input('Insira a média do aluno: '))

print('-' * 20)

print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["media"]}')
if aluno['media'] >= 7:
    print('Situação: Aprovado!')
else: 
    print('Situação: Reprovado!')

print('-' * 20)