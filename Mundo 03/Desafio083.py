#Exercício083

listaexp = []
expressao = str(input('Insira a expressão: '))

for simbolo in expressao:
    if simbolo == '(':
        listaexp.append('(')
    elif simbolo == ')':
        if len(listaexp) > 0:
            listaexp.pop()
        else:
            listaexp.append(')')
            break
if len(listaexp) == 0:
    print('Expressão válida!')
else: 
    print('Expressão inválida!')
