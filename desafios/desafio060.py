inicial = int(input('Digite um número para saber o valor do seu fatorial: '))
num = inicial
fatorial = 1
while num != 0:
    fatorial *= num
    num -= 1
print(f'{inicial}! = {fatorial}')
