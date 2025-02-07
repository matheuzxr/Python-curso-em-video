casa = float(input('Qual o valor da casa que você deseja comprar? R$'))
sal = float(input('Qual o valor do seu salário? R$'))
tempo = int(input('Informe em quantos anos você pretende quitar a casa: '))
prestacao = casa / (tempo * 12)
if prestacao <= 30/100 * sal:
    print(f'Empréstimo aprovado com prestações de R${prestacao:.2f}')
else:
    print('Empréstimo negado.')
