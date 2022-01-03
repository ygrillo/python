'''
Refaça o Desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
Ex. 35:
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo.
'''

a = int(input('Primeira reta: '))
b = int(input('Segunda reta: '))
c = int(input('Terceira reta: '))

#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b

if (b - c) < a and a < (b + c):
    if (a - c) < b and b < (a + c):
        if (a - b) < c and c < (a + b):
            if a == b and b == c:
                print('Elas \033[32mformam\033[m um triângulo \033[4mequilátero!')
            elif a == b or a == c or b == c:
                print('Elas \033[32mformam\033[m um triângulo \033[4misósceles!')
            elif a != b and b != c and c != a:
                print('Elas \033[32mformam\033[m um triângulo \033[4mescaleno!')
        else:
            print('Elas \033[31mNÃO\033[m formam um triângulo')
    else:
        print('Elas \033[31NÃO\033[m formam um triângulo')
else:
    print('Elas \033[31NÃO\033[m formam um triângulo')