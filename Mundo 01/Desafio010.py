#Desafio0010

print('Converta reais para dólar e euros. ')


valor = float(input('Quanto você tem? R$'))
dolar = float('5.37') # dia: 16/02/2021 // vídeo: 3.37
euros = float('6.53') # dia: 16/02/2021 

# print('Com RS${:.2} você pode comprar US${:.2}'.format(valor, valor/dolar)) 
print('com R${:.2f} você pode comprar US${:.2f} dólares e €{:.2f}. '.format(valor, valor/dolar, valor/euros))

