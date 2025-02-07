nome = ''
idade = 0
sexo = ''
soma = 0
velho = 0
homem = ''
mulheresjovens = 0
for i in range(0, 4):
    nome[i] = input(f'Nome da pessoa {i+1}: ').title()
    idade[i] = int(input(f'Idade da pessoa {i+1}: '))
    sexo[i] = input(f'Sexo da pessoa {i+1} (M/F): ').upper()
    soma += idade[i]
    if idade[i] > velho:
        velho = idade[i]
        homem = nome[i]
    elif sexo == F and idade < 20:
        mulheresjovens += 1
print(f'Média das idades: {soma/4} \nHomem mais velho: {homem} \nMulheres com menos de 20 anos: {mulheresjovens}')