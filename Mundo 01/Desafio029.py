#Desafio029

velocidade = float(input('Qual é a velocidade em que seu carro andou? '))

pagar = (velocidade-80)*7

if velocidade > 80 :
    print(f'Um momento! Você estava acima de velocidade permitida. Pague R${pagar:.2f}!!!')
print('Tenha um bom dia!')
#else:
    #print('Tranquilo! Continue andando na velocidade permitida.')
