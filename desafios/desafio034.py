sal = float(input('Informe o seu salário: '))
if sal <= 1412:
    aumento = 15/100 * sal
else:
    aumento = 10/100 * sal
print('Seu salário com aumento será R${:.2F}' .format(sal + aumento))
