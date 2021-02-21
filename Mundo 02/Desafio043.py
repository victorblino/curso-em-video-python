#Desafio043

peso = float(input('Insira seu peso em KG: '))
altura = float(input('Insira sua altura: '))

imc = peso / (altura * altura)

print(f'O seu IMC é de: {imc:.2f}')

if imc < 18.5: 
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc <= 30:
    print('Você está no sobrepreso!')
elif imc >= 30 and imc <=40:
    print('Você está na obesidade!')
elif imc >= 40:
    print('Você está na obesidade mórbida!')
