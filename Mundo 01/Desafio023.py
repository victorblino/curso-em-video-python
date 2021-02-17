#Desafio023

n = int(input('Insira um número: '))
#num = str(n)

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f"""Analisando...

Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}

""")


'''print(f"""Analisando...

Unidade: {n[0]}
Dezena: {n[1]}
Centena: {n[2]}
Milhar: {n[3]}

""")'''

