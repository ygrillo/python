#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere: US$1 = R$3,27

wallet = float(input('Quantos reais você possui? R$'))
dolar = wallet/3.27

print(f'Você pode comprar US${dolar:.2f}')