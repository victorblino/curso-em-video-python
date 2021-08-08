#Exercício107

from utilidadescev import moeda
from utilidadescev.dado import leiaDinheiro

valor = leiaDinheiro('Digite o valor: R$')
moeda.resumo(valor, 10, 30)
