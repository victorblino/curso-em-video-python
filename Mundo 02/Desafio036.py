#Desafio036

valorcasa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? RS$'))
anos = float(input('Por quantas parcelas você vai pagar? '))

prestacaomensal = valorcasa / (anos * 12)

excedido = salario / 30 * 100

print(f'Para você pagar uma casa com valor de R${valorcasa:.2f} em {anos} anos com R${salario:.2f} você precisará pagar de um valor mensal de {prestacaomensal:.2f}')

if prestacaomensal > salario:
    print('Seu empréstimo foi negado!')
else: 
    print('Empréstimo bem sucedido!')


