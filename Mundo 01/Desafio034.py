#Desafio034

salario = float(input('Qual é o seu salário? '))


if salario >= 1250:
    novo = salario + (salario * 10 /100)
    print(f'O seu salário recebeu um aumento de 15%! Agora, você recebe R${novo}!')
else:
    novo = salario + (salario * 10 / 100)
  
    print(f'O seu salário recebeu um aumento de 10%! Agora, você recebe R${novo}!')

