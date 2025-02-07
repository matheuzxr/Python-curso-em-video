soma = mil = cont = anterior = 0
while True:
    produto = input(f'Nome do produto {cont+1}: ').title()
    preco = float(input('Preço: '))
    soma += preco
    if preco >= 1000:
        mil += 1
    if preco < anterior:
        barato = produto
        baratoPreco = preco
    anterior = preco
    prosseguir = ''
    while prosseguir not in ['S', 'N']:
        prosseguir = input('Deseja cadastrar mais produtos? [S/N]: ').upper()
    if prosseguir == 'N':
        break
    cont += 1
print(f'Total: R${soma:.2f} \nProdutos a partir de R$1000: {mil} \nProduto mais barato: {barato} - R${baratoPreco:.2f}')
