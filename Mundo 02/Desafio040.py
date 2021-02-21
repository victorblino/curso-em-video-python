#Desafio040

n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

media = (n1+n2) / 2

if media < 5:
    print('O aluno está reprovado!')
elif media >= 5 and media <= 6.9:
    print('O aluno está em recuperação!')
else:
    print('O aluno foi aprovado!')

