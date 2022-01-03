#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
#deles e escrevendo o nome do escolhido.

from random import choice

n1 = input('Digite o nome do primeiro: ')
n2 = input('Do segundo: ')
n3 = input('Do terceiro: ')
n4 = input('Do quarto: ')

lista = [n1, n2, n3, n4]    #cria uma lista com os nomes inseridos

print(f'O aluno escolhido foi: {choice(lista)}') #escolhe o nome na lista
