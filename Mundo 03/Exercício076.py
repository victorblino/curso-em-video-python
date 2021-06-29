#Exercício076

valores = (
    int(input('Insira um número: ')), 
    int(input('Insira outro número: ')),
    int(input('Insira o penúltimo valor: ')),
    int(input('Insira o último: '))
)

cont = 0

print(f'O número nove apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 foi digitado na {valores.index(3)+1} posição.')
else:
    print('O número três não foi digitado nenhuma vez.')
print('Os valores pares digitados, foram: ', end='')

for n in valores:
    if n % 2 == 0:
        print(n, end=' ')

