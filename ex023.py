#Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos digitos separados (string e matemáticamente)

import random

numero = input('Digite um número: ')

print(numero)

# Por String

numerostr = str(numero)

print(
    'Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(numerostr[3],numerostr[2],numerostr[1],numerostr[0])
)

print(numerostr[0])

# Por matemática é possivel adicionar números menor que 1000


