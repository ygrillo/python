'''
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
            print('Elas formam uma reta!')
        else:
            print('Elas não formam uma reta')
    else:
        print('Elas não formam uma reta')
else:
    print('Elas não formam uma reta')