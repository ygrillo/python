#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Seu salário: R$'))

aum = sal+(0.15*sal)

print(f'Salário com aumento de 15%: R${aum:.2f}')