#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


while True:
    distancia = int(input('Qual a distância da viagem: '))

    if distancia <= 200:
        print('O preço da passagem é R$ {:.2f}'.format(distancia*0.5))

    else:
        print('O preço da passagem é R$ {:.2f}'.format(distancia*0.45))