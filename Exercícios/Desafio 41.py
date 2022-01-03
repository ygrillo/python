'''
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
'''

lista = ['Mirim', 'Infantil', 'Junior', 'Sênior', 'Master']

ano_nasc = int(input('Ano de nascimento: '))

idade = 2017 - ano_nasc

if idade <= 9:
    print(f'Categoria: {lista[0]}')
elif idade <= 14:
    print(f'Categoria: {lista[1]}')
elif idade <= 19:
    print(f'Categoria: {lista[2]}')
elif idade <= 20:
    print(f'Categoria: {lista[3]}')
else:
    print(f'Categoria: {lista[4]}')