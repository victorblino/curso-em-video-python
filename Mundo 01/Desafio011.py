#Desafio011

altura = float(input('Insira uma altura (em metros): '))
base = float(input('Insira uma largura (em metros): '))
area = base*altura

print('\nÁrea: {}m²\nQuantidade de latas de tinta para pintar a parede: {} latas.'.format(area, area/2))
