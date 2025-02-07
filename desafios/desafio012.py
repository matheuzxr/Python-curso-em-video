preco = float(input('Qual o valor do produto?'))
desconto = preco - (5/100 * preco)
print('O produto com desconto fica R${:.2f}' .format(desconto))