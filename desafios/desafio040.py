n1 = float(input('Nota da Prova 1: '))
n2 = float(input('Nota da Prova 2: '))
media = (n1+n2)/2
if media >= 6:
    print('Aluno aprovado.')
elif 4 <= media <= 6:
    print('Aluno de recuperação.')
else:
    print('Aluno reprovado.')
