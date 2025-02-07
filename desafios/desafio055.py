maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input(f'Informe o peso da pessoa {i+1}: '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'Maior peso {maior}kg \nMenor peso: {menor}kg')