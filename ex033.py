#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

import random

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

numeros = [n1,n2,n3]

numord = sorted(numeros)

print(numeros)

print(f'O menor número é {numord[0]}')
print(f'O maior número é {numord[-1]}')