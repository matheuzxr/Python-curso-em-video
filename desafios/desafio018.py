import math
ang = float(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = sen/cos # tg2 = math.tan(ang)
print('Seno: ', sen,
      'Cosseno: ', cos,
      'Tangente: ', tg)
