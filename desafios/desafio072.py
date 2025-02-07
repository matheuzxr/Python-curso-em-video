extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
user = int(input('Digite um número de 0 a 20: '))
while user not in range(0, 21):
    user = int(input('Digite um valor válido: '))
print(f'Você digitou o número {extenso[user]}')