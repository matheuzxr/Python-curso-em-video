idade = int(input('Informe a sua idade: '))
if idade < 18:
    print('Ainda não é hora de se alistar.')
    print('Você deverá se alistar daqui {} anos.' .format(18-idade))
elif idade == 18:
    print('Já está na hora de se alistar.')
else:
    print('Já passou da hora de voce se alistar.')
    print('Você deveria ter se alistado a {} anos atras' .format(idade-18))
