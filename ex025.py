#Cria um programa que leia o nome de uma cidade e diga se ela tem "SILVA" no nome

while True:

    cidade = input('Digite o nome: ')

    #cidade = input('Digite uma cidade:')

    #cidadesep = (cidade.split())

    print(cidade)

    cidadelow = cidade.lower()

    if 'silva' in cidadelow:
        print('O nome {} TEM \033[32m"SILVA"\033[m'.format(cidade))

    else:
        print(f'A cidade {cidade} NÃO inicia com "SANTO"')

