#Desafio027

nome = str(input('Olá! Qual é seu nome? ')).strip().split()

print(f"""É um prazer te conhecer!
O seu primeiro nome é: {nome[0]}
Seu último nome é: {nome[len(nome)-1]}""")
