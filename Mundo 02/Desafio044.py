#Desafio044

compra = float(input('Qual é o preço da compra? R$'))
pagamento = int(input("""-- Qual será a forma de pagamento? --
[1] Á vista dinheiro/cheque
[2] Á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Opção:"""))

if pagamento == 1:
    valor = compra - ((compra * 10) / 100) 
    print(f'Você terá um desconto de 10%! Total: R${valor:.2f}')
elif pagamento == 2:
    valor = compra - ((compra * 5) / 100)
    print(f'Você terá um desconto de 5%! Total: R${valor:.2f}')
elif pagamento == 3:
    valor = compra / 2
    print(f'Você irá pagar R${valor:.2f} por mês sem juros. Total: R${valor:.2f}')
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas? '))
    valor = (compra + ((compra * 20) / 100)) / parcelas
    print(f'Você terá 20% de juros! Você irá pagar R${valor:.2f} por mês. Total: R${valor:.2f}')
else:
    print('Opção inválida! Tente novamente.')
