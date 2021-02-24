#Desafio051

print('--- 10 termos de uma PA ---')

n = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
decimo = n + (10 - 1)*razao

for pa in range(n, decimo + razao, razao):
    print(pa, end=' -> ')
print('Acabou :)')