# Faça um programa que leia o comprimento do cateto oposto e de cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math;

ca = float(input('Digite o cateto ADJACENTE:'))
co = float(input('Digite o cateto OPOSTO:'))

hip = math.sqrt(pow(ca,2)+pow(co,2))

print(hip)