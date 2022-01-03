'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7 por cada Km acima do limite.
'''

vel = int(input('Digite a velocidade: '))   #vel recebe a velocidade em que o carro está

if vel > 80:
    multa = (vel-80) * 7
    print(f'Você foi multado em R${multa}!')
else:
    print('Você está na velocidade permitida')