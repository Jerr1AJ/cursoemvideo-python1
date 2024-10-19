#Crie um programa que leia um núimero inteiro e mostre na tela se ele é par ou ímpar

while True:
    
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        print(f'O número {numero} é PAR!')

    else:
        print(f'O número {numero} é IMPAR!')