#Desafio064

cont = 0
total = 0
soma = 0
n = 0

while n != 999:
    n = int(input('Insira um número [999 para parar]:'))
    soma +=n
    cont+=1
print(f'Você digitou {cont} números e a soma é {soma-999}.')