#Desafio067

while True:
    n = int(input('Você quer a tabuada de qual valor? R: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} * {c} = {n*c}')

print('PROGRAMA ENCERRADO')