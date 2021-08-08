#Exercício105

def notas(* n, situação=False):

    """
    Programa que mostra :
    - O total de notas inseridas;
    - A maior nota;
    - A menor nota;
    - A média;
    - Situação (Opcional)
    """

    notasAlunos = dict()

    notasAlunos['total'] = len(n)
    notasAlunos['maior'] = max(n)
    notasAlunos['menor'] = min(n)
    notasAlunos['média'] = sum(n)/len(n)

    if situação:
        if notasAlunos['média'] >= 7:
            notasAlunos['situação'] = 'Boa!'
        if notasAlunos >= 5:
            notasAlunos['situação'] = 'Razoável!'
        else:
            notasAlunos['situação'] = 'Ruim!'
    return notasAlunos        

print(notas(5, 5.5, 2, 7.5, 8, 9.5))