def leiaDinheiro(msg):
    válido = False
    while not válido:
        valor = str(input(msg).replace(',', '.'))
        if valor.isalpha() or valor.strip() == '':
            print('Valor inválido! Por favor, insira um valor válido!')
        else:
            válido = True
            return float(valor)
