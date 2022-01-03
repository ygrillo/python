#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex.: Digite um número: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

import random

#Método matemático
#Método por String não dá por enquanto...
num = random.randint(0, 9999)   #Escolhe um número aleatório entre 0 e 9999

print(f'Número: {num}') #Mostra na tela o número escolhido

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')