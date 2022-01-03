#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
#e mostre o comprimento da hipotenusa.

from math import hypot, sqrt

co = float(input('Valor do Cateto Oposto: '))
ca = float(input('Valor do Cateto Adjacente: '))

#h = sqrt(pow(co,2)+pow(ca, 2)) -> sem usar o módulo
h1 = hypot(co, ca) # usando o módulo

print(f'O valor da Hipotenusa é: {h1:.2f}')