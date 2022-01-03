'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

import emoji

ano_nasc = int(input('Ano de nascimento: '))

if ano_nasc == 2000:
    print(emoji.emojize('Está na hora de se alistar! :smile:', use_aliases=True))
elif ano_nasc > 2000:
    alistar = 18 - (2017 - ano_nasc)
    print(emoji.emojize(f'Falta {alistar} anos para você se alistar :wink:', use_aliases=True))
elif ano_nasc < 2000:
    p_alistar = (2017 - ano_nasc) - 18
    print(emoji.emojize(f'Já passou {p_alistar} anos de se alistar! :anguished:', use_aliases=True))