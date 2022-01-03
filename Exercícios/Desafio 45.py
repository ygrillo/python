'''
Crie um programa que faça o computador jogar jokenpô com você.
'''

import random
import emoji

p1 = int(input(emoji.emojize(':fist: - 1\n:hand: - 2\n:v: - 3\nSua vez: ', use_aliases=True)))

p2 = random.randint(1, 3)
print(f'Vez do adversário: {p2}')

if p1 == p2:
    print('\033[43mEMPATE!\033[m')
elif p1 == 1 and p2 == 2:
    print('VOCÊ PERDEU!')
elif p1 == 1 and p2 == 3:
    print('VOCÊ VENCEU!')
elif p1 == 2 and p2 == 1:
    print('VOCÊ VENCEU!')
elif p1 == 2 and p2 == 3:
    print('VOCÊ PERDEU!')
elif p1 == 3 and p2 == 1:
    print('VOCÊ PERDEU!')
elif p1 == 3 and p2 == 2:
    print('VOCÊ VENCEU!')
else:
    print('SOMENTE PEDRA, PAPEL OU TESOURA!')