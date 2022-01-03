'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
'''

num = int(input('Digite um número inteiro: '))

base_conv = int(input('Escolha a base de conversão:\n1 para binário\n2 para octal\n3 para hexadecimal\nNúmero: '))

if base_conv == 1:
    print(f'O número binário é: {bin(num)}')
elif base_conv == 2:
    print(f'O número octal é: {oct(num)}')
elif base_conv == 3:
    print(f'O número hexadecimal é: {hex(num)}')
else:
    print('Reinicie o programa e coloque um valor de conversão válido!')

