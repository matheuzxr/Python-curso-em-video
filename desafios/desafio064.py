num = int(input('Digite um número qualquer (para parar digite 999): '))
soma = 0
cont = 0
while num != 999:
    soma += num
    num = int(input('Próximo: '))
    cont += 1
print(f'Soma total = {soma} \nNúmeros informados: {cont}')
