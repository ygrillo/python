'''
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
'''

num = int(input('Digite o número: '))

if (num % 2) == 0:      #O resto da divisão do num por 2 é igual a 0?
    print(f'{num} é par!')
else:
    print(f'{num} é ímpar!')