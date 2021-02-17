#Desafio026 

frase = str(input('Insira uma frase: ')).lower().strip()

print(f"""A letra A aparece: {frase.count('a')} vezes
A letra A aparece primeiro na posição {frase.find('a')+1}
Ela aparece por último na posição {frase.rfind('a')+1}
""")
