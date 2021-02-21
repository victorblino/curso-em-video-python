#Desafio037

n = int(input('Insira algum número: '))
escolha = int(input("""Escolha a opção:
[1] BINÁRIO
[2] OCTAL
[3] DECIMAL
Opção: """))

if escolha == 1:
    print(f'Binário: {bin(n)[2:]}')
elif escolha == 2:
    print(f'Octal: {oct(n)[2:]}')
elif escolha == 3:
    print(f'Hexadecimal: {hex(n)[2:]}')
else:
    print('Nenhuma escolha!')


    