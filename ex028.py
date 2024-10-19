# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrevar na tela se o usuário venceu ou perdeu

import random

numero = random.randint(0,5)

print(numero)


while True:
    escolha = int(input('Escolha um número: '))
   
    if numero == escolha:
        print('Parabens, você acertou!')
    

    else:
        print('Tente novamente')