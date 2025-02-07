nome = input('Digite seu nome: ').strip().title().split()
print('Primeiro nome: {}' .format(nome[0]),
      '\nÚltimo nome: {}' .format(nome[len(nome) - 1]))
