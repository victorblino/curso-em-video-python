#Desafio031

distancia = float(input('Qual foi a distância percorrida na viagem? '))

if distancia <= 200:
    print(f'Você irá ter que pagar R${distancia*0.50}!')

else:
    print(f'Você irá ter que pagar R${distancia*0.45}')