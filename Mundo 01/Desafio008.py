#Desafio 008

m = float(input('Escreva um valor em metros:'))

km = m/1000
hm = km*10
dam = hm*10
dm = m*10
cm = dm*10
mm = cm*10


print('{} metros é igual a: {}km, {}hm, {}dam, {}dm, {}cm, {}mm.'.format(m, km, hm, dam, dm, cm, mm))