#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO"

while True:

    cidade = input('Digite uma cidade:')




    cidadesep = (cidade.split())

    print(cidadesep)

    if cidadesep[0].lower() == 'santo':
        print('A cidade de {} inicia com "SANTO"'.format(cidade))

    else:
        print(f'A cidade {cidade} NÃO inicia com "SANTO"')



#Cria um programa que leia o nome de uma cidade e diga se ela tem "SILVA" no nome


#Faça um programa que leia uma frase pelo teclado e mostre:
#1.Quantas vezxes aparece a letra "A";2.Em que posição ela aparece pela primeira vez;3.Em que posição ela aparece a última vez


#Faça um p´rograma que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadmente