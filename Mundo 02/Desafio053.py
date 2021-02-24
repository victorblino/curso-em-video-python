#Desafio053

frase = str(input('Insira uma frase e veja se ela é palindroma: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''



for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print(f'Frase digitada: {junto}\nFrase invertida: {inverso}\n')

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palímentro!')
