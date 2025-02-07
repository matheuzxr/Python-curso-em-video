lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
# tuplas são imutáveis
for comida in lanche:
    print(f'{comida} é muito bom')

for pos, comida in enumerate(lanche):
    print(f'eu gosto de {comida} na pos {pos}')

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]}')