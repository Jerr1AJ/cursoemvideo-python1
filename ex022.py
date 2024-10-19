#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1.O nome com todas as letras maiúsculas; 2.O nome com todas minúsculas;3.Quantas letras ao todo sem considerar espaços;4.Quantas letras tem o primeiro nome

nome = input("Digite seu nome:")
#nome = "Jerry Augusto Macedo dos Santos Junior"

print(nome.upper())     #[1]

print(nome.lower())     #[2]

nomepart = nome.split()

print(len(nome) - nome.count(" "))  #[3]

print(len(nomepart[0]))     #[4]

