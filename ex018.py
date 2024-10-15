# Faça um prograMa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

ang = float(input('Digite o valor do ângulo'))

radian = math.radians(ang)

print('Seno {}'.format(math.sin(radian)))
print('Cosseno {}'.format(math.cos(radian)))
print('Tangente {}'.format(math.tan(radian)))