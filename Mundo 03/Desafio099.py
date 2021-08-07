#Exercício099

def maior(* n):
    print('-' * 20)
    print(f'Números inseridos: {n}')
    print(f'O maior número dessa lista é {max(n)}')
    print('-' * 20)

maior(0, 5, 4, 2, 1)
maior(3, 2, 9, 4)
maior(1, 0, 6)
maior(1, 4)
