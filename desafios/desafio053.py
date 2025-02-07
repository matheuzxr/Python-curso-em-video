frase = input('Digite uma frase qualquer (apenas letras): ')
analise = frase.replace(' ', '').upper()
tamanho = len(analise) - 1
inverso = ''
for i in range(tamanho, -1, -1):
    letra = analise[i]
    inverso += letra.upper()
if analise == inverso:
    print(f'{analise} é um palíndromo!')
else: 
    print(f'{analise} não é um palíndromo! Seu inverso é {inverso}')