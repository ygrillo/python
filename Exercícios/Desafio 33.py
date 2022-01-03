'''
Faça um programa que leia quatro números e mostre qual é o maior e qual é o menor.
'''

a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))
d = int(input('Quarto: '))

#verifica quem é maior

maior = a

if b > a and b > c and b > d:
    maior = b
if c > a and c > b and c > d:
    maior = c
if d > a and d > b and d > c:
    maior = d

#verifica quem é o menor

menor = a

if b < a and b < c and b < d:
    menor = b
if c < a and c < b and c < d:
    menor = c
if d < a and d < b and d < c:
    menor = d

print(f'Número maior: \033[1;31m{maior}\033[m\nNúmero menor: \033[1;34m{menor}\033[m')