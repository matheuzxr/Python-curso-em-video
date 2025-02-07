classificacao = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo',  'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print('Os 5 primeiros colocados são: ', end='')
for times in classificacao[:5]:
    print(times, end=' ')

print('\nOs últimos 4 colocados são: ', end='')
for times in classificacao[-4:]:
    print(times, end=' ')

print(f'\nOs times em ordem alfabética: {sorted(classificacao)}')

print(f'O Atlético-MG está na posisão {classificacao.index('Atlético-MG') + 1} do ranking.')