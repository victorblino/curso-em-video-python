#Exercício106

def ajuda(comando):
    print('')
    help(comando)
    print('')

def titulo(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))

while True:
    print(titulo('Sistema de Ajuda Python'))
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

# Vai ficar assim, por enquanto, não tô com saco pra fazer o resto agora (3 da manhã...)