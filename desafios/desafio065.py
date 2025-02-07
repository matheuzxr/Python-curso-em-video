cont = 0
soma = 0
continuar = ''
while continuar in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    continuar = input('Deseja continuar? [S/N] ')
media = soma / cont 
print('Média dos {} valores: {}' .format(cont, media))
