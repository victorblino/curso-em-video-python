#Desafio013

salarioinicial = float(input('Insira o salário do funcionário: '))
salarioaumento = 15*salarioinicial/100
salariofinal = salarioinicial+salarioaumento

print('O salário final do funcionário com 15% de aumento será: R${:.2f}'.format(salariofinal))