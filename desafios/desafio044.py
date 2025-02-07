preco = float(input('Digite o preço do produto: '))
print('1 – à vista dinheiro/pix'
      '2 – à vista no cartão'
      '3 – em até 2x no cartão'
      '4 – 3x ou mais no cartão')
pag = int(input('Condição de pagamento: '))
if pag == 1:
    precoDesc = preco - (10/100 * preco)
    print(f'Preço com desconto: R${precoDesc:.2f}')
elif pag == 2:
    precoDesc = preco - (5/100 * preco)
    print(f'Preço com desconto: R${precoDesc:.2f}')
elif pag == 3:
    print(f'Preço sem alteração: R${preco:.2f}')
elif pag == 4:
    precoJuros = preco + (20/100 * preco)
    print(f'Preço com juros: R${precoJuros:.2f}')
else:
    print('Condição de pagamento não encontrada, tente novamente.')
