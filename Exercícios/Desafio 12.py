#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input('Preço original: R$'))

newprice = prod-(0.05*prod)

print(f'Preço com desconto de 5%: R${newprice}')