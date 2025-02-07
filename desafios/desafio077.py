palavras = ('abacaxi', 'bola', 'celular', 'cobertoe', 'lugar', 'encontrar', 'estacionamento', 'sombra')
vogais = ('a', 'e', 'i', 'o', 'u')
for i in palavras:
    print('\n', i, end=': ')
    for j in vogais:
        if j in i:
            print(j, end=' ')