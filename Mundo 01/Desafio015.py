#Desafio015

dAlugados = int(input('Quantos dias você alugou o carro? '))
kmAndados = float(input('Quantos km você andou? '))

valor = (dAlugados*60) + (kmAndados*0.15)

print('Você irá ter que pagar: R${:.2f}'.format(valor))

