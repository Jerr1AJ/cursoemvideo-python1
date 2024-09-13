# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabewndo que cada litro de tinta pinta 2 m2

largura = float(input('Digite a largura da parede:'))
altura =  float(input('Digite a altura da parede:'))

area = largura*altura

print(area)

print('Sabendo que a parede mede {:.2f} metros quadrados \nentão serão necessárias {} latas de tinta para pinta-lá'.format(area,int(area/2)))

# Faça um algoritmo que leia op preçlo de um de um produto e mostre seu novo preço, com 5% de desconto

# Faça um algotirmo que leia o salário de um funcionário e mostre seu novo saláriop, com 15% de aumento.