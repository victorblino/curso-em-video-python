#Desafio066

soma = cont = 0

while True:
    n = int(input('Insira um número: '))
    if n == 999:
        break
    soma+=n
    cont+=1
print(f'Você digitou {cont} números e a soma total entre eles é: {soma}')