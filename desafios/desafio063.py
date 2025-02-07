total = int(input('Digite quantos elementos da sequência de Fibonacci deseja visualizar: '))
n1 = 0
n2 = 1
cont = 0
print(n1, n2, end=' ')
while cont < total:
    prox = n1 + n2
    print(prox, end=' ')
    n1 = n2
    n2 = prox
    cont += 1
print('Fim')