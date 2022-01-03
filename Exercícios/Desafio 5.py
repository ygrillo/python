# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
#informações possíveis sobre ele.

algo = input('Digite algo: ')
print('É do tipo', type(algo))
print('Está em letra maiúscula? ', algo.isupper())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())