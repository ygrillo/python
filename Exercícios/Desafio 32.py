'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

ano = int(input('Digite o ano: '))

if (ano % 4) == 0:
    if (ano % 100) != 0:
        print(f'{ano} é bissexto!')
    elif (ano % 400) == 0:
        print(f'{ano} é bissexto!')
    else:
        print(f'{ano} NÃO é bissexto')
