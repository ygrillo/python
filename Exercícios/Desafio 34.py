'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%
'''

sal = float(input('Digite seu salário: '))

if sal > 1250:
    aumento = sal*1.1
    print(f'Com o aumento foi para: R${aumento:.2f}')
else:
    aumento = sal*1.15
    print(f'Com o aumento foi para: R${aumento:.2f}')