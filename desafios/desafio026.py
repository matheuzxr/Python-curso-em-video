frase = input('Digite uma frase qualquer: ').lower().strip()
print('A letra a aparece {} vezes nessa frase.' .format(frase.count('a')))
print('Primeira ocorrência: {}º posição' .format(1 + frase.find('a')),
      '\nÚltima ocorrência: {}º posição' .format(1 + frase.rfind('a')))
