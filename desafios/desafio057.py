sexo = input('Informe o seu sexo (M/F): ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Inválido. Tente novamente: ').upper()
print('Válido.')
