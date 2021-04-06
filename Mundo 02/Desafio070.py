#Desafio070

print('-- LOJA --')

soma = produtosCaros = cont = menor = 0
produtoMaisBarato = ' '

while True:
    nomeProduto = str(input('Insira o nome do produto: '))
    preçoProduto = float(input('Insira o preço do produto: '))
    soma =+ preçoProduto
    if preçoProduto > 1000:
        produtosCaros+=1
    if cont == 1:
        menor = preçoProduto
    else:
        if preçoProduto < menor:
            menor = preçoProduto
            produtoMaisBarato = nomeProduto
    resp = ' '

    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
    if resp == 'N':
        break

    
    
print(f'O total gasto na compra é R${soma}. {produtosCaros} produtos custaram mais do que R$1000. O produto mais barato é {produtoMaisBarato} que custa R${menor}')