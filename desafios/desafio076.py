produtos = ('Arroz', 11.98, 'Feijão', 6.29, 'Macarrão', 4.00, 'Açucar', 10.50, 'Sal', 4.99, 'Ovo', 14.98, 'Leite', 6.70, 'Óleo', 7.70, 'Farinha', 3.00, 'Suco', 9)
print('-'*40)
print(f"{'Tabela de preços':^40}")
print('-'*40)
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<30}R${produtos[i+1]:>6.2f}')
print('-'*40)
