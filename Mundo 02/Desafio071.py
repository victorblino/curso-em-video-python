#Desafio071

print('-- BANCO DO BRASIL --')

valor = int(input('Quanto você quer sacar? R: '))

total = valor
cédula = 50
totalCédula = 0

while True:
    if total >= cédula:
        total -= cédula
        totalCédula+=1
    else: 
        if totalCédula > 0:
            print(f'{totalCédula} cédulas de {cédula} reais.')
        if cédula == 50:
            cédula == 20
        if cédula == 20:
            cédula == 10
        if cédula == 10:
            cédula == 1 
        totalCédula == 0
        if total == 0:
            break
