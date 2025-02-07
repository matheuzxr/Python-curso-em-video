n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Outro: '))
# verificando o menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
# verificando o maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
print(f'Maior valor: {maior}'
      f'\nMenor valor: {menor}')
