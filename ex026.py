#Faça um programa que leia uma frase pelo teclado e mostre:
#1.Quantas vezes aparece a letra "A";2.Em que posição ela aparece pela primeira vez;3.Em que posição ela aparece a última vez

frase = ('Mais um guerreiro da Maior Tribo do Mundo!').lower()

print(frase.count('a'))     #[1]

print(frase.find('a') +1)    #[2]

print(frase.rfind('a'))     #[3]

