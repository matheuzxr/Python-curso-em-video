from random import choice
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
a5 = input('Nome do aluno 5: ')
lista = [a1, a2, a3, a4, a5]
sorteado = choice(lista)
print('O aluno sorteado é', sorteado)