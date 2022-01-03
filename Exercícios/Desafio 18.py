#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo: '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))

print(f'Seno: {sen:.2f}\nCosseno: {cos:.2f}\nTangente: {tg:.2f}')
