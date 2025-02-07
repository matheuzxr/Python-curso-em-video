from math import sqrt
adj = float(input('Digite o valor do cateto adjacente: '))
opt = float(input('Digite o valor do cateto oposto: '))
hip = sqrt(pow(adj, 2) + pow(opt, 2)) # hypot poderia ter sido importada
print('A hipotenusa vale {}.' .format(hip))