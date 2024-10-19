#Escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite

while True:
    vel = int(input('Qual a velocidade:'))
    vel_maxima = 80

    if vel > vel_maxima:
        print('Você foi Multado! O valor da multa é R$ {:.2f}'.format((vel-vel_maxima)*7))
    else:
        print('Você está dentro do limite de velocidade, Parabéns!')