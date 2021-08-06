#Exercicio089

alunos = list()
alunosGerais = list()

while True:
    nomeAluno = str(input('Insira o nome do aluno: '))
    alunos.append(nomeAluno)
    n1 = float(input('Insira a primeira nota: '))
    alunos.append(n1)
    n2 = float(input('Insira a segunda nota: '))
    alunos.append(n2)
    media = (n1+n2)/2
    alunos.append(media)

    alunosGerais.append(alunos[:])
    alunos.clear()

    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break

print('-' * 20)

for a in range(0, len(alunosGerais)):
    print(f'Aluno {a+1}:\n')
    print(f'Nome : {alunosGerais[a][0]}')
    print(f'Média: {alunosGerais[a][3]}')
    print('-' * 20)

while True:
    r = int(input('Deseja acessar a nota de qual aluno? (Insira 999 caso queira interromper o programa.) '))
    if r == 999:
        break
    print(f'Aluno {r}: \n')
    print(f'Nota 1: {alunosGerais[r-1][1]}')
    print(f'Nota 2: {alunosGerais[r-1][2]}')
    print('-' * 20)

# Esse código pra mim foi o mais gostoso de fazer. A solução do Guanabara é mais enxuta mas eu achei a melhor a minha, porque ficou melhor de entender o código.