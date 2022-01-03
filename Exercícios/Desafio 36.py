'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

#Aprovador de empréstimo bancário

valor_casa = float(input('Valor da casa: '))
sal = float(input('Salário: '))
time = int(input('Em quantos anos? '))

prest_mensal = valor_casa/(time*12)

if prest_mensal > (0.3*sal):
    print('Empréstimo \033[1;31mNEGADO\033[m')
else:
    print('Empréstimo \033[1;32mACEITO\033[m\nValor da prestação: R${:.2f}'.format(prest_mensal))