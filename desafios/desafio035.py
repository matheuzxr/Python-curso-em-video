from math import sqrt
r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))
if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    print('Essas retas PODEM formar um triângulo.')
    s = (r1+r2+r3)/2 # semiperimetro do triangulo
    a = sqrt(s*(s-r1)*(s-r2)*(s-r3)) # area do triangulo
    print(f'A área desse triângulo mede {a}.')
else:
    print('É impossível formar um triângulo com essas retas.')
