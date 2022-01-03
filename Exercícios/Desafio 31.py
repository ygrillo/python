'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''

dist = int(input('Digite a distância da viagem: ')) #dist recebe a distância da viagem

if dist <= 200:
    price = dist*0.50
    print(f'O preço da passagem ficou em: R${price}')
else:
    price = dist*0.45
    print(f'O preço da passagem ficou em: R${price}')