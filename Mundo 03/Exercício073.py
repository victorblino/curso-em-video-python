#Desafio073

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinte', 'dezesseis', 'dezessete', 'dezoito,', 'dezenove', 'vinte')


while True:
    n = int(input('Insira um número de 1 a 20 para eu mostrar em extenso! '))
    if 0 <= n <= 20:
        break
    print('Tente novamente!')
print(f'O número {n} por extenso é: {numeros[n]}')