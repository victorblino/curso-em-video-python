#Desafio004

n = input('Escreva algo e verifique as caracteristicas: ')

print('O tipo primitivo desse valor é: {}\nContém somente letras? {}\nContém somente números? {}\nContém somente letras e números? {}\nContém somentes dígitos? {}\nEstá em minúsculo? {}\nEstá em maisúsculo? {}\nContém somente espaço? {}\nEstá capitalizada? {}'.format(type(n), n.isalpha(), n.isnumeric(), n.isalnum(), n.isdigit(), n.islower(), n.isupper(), n.isspace(), n.istitle()))

#No caso, eu não quis fazer um monte de print porque achei desnecessário :/ Mas cada linha ficaria com print('É tal tal tal?', n.isExemplo())