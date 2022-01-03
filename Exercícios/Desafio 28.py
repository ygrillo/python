#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0, 5)  #Gera um número inteiro aleatório entre 0 e 5

chute = int(input('Chute o número escolhido: '))
if chute == num:
    print(f'Você acertou!')
else:
    print(f'Você errou. Era o número {num}')