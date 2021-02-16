#Desafio022

nome = str(input('Qual é o seu nome completo? ')).strip()

print(f"""Nome em maiúsculo: {nome.upper()}
Nome em minúsculo: {nome.lower()}
Seu nome tem: {len(nome)-nome.count(' ')} letras
Quantas letras tem o primeiro nome: {nome.find(' ')} letras """)