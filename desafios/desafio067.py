while True:
    num = int(input('Digite de qual número você quer saber a tabuada (negativo para encerrar): '))
    if num < 0:
        break
    print(f'Tabuada do {num}')
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
print('Encerrando a tabuada')
