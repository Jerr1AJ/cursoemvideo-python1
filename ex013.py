# Faça um algotirmo que leia o salário de um funcionário e mostre seu novo saláriop, com 15% de aumento.

salario = float(input('Qual o salário atual? R$ '))
                
aumento = salario*1.15

print('Seu novo salário é de R${:.2f}'.format(aumento))