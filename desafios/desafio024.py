cidade = input('Informe sua cidade: ').lower()
split = cidade.split()
print('O nome dessa cidade começa com santo:', 'santo' in split[0])