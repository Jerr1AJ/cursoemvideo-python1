# Um professor que sortear um dos seus quatro alunos para apagar o quadreo. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

a1 = input('Digite o primeiro aluno')
a2 = input('Digite o segundo aluno')
a3 = input('Digite o terceiro aluno')
a4 = input('Digite o quarto aluno')

alunos = [a1,a2,a3,a4]


print(random.choice(alunos))


# O mesmo professor do desafio anterior que sortear a ordem de apresentação de trablhos dos alunos. Faça um programa que leia o nome dos quadtros alunos e mostre a ordem sortada

print('a ordem é {}'.format(random.sample(alunos)))

