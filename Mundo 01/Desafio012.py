#Desafio012

valorinicial = float(input('Insira o preço do produto: '))
valordesconto = float(5*valorinicial/100)
valorfinal = valorinicial-valordesconto


print('O valor com 5% de desconto é: R${:.2}'.format(valorfinal))