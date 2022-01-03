'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

normal_price = float(input('Preço normal: R$'))
cond = int(input('Condição de pagamento:\n1 - À vista (dinheiro ou cheque): 10% OFF\n2 - À vista (cartão): 5% OFF\n3 - Em 2x: preço normal\n4 - 3x ou mais: 20% de Juros\nOpção: '))

if cond == 1:
    valor_f = normal_price - (0.1 * normal_price)
    print(f'Valor final: R${valor_f}')
elif cond == 2:
    valor_f = normal_price - (0.05 * normal_price)
    print(f'Pagamento: 1 Parcela de R${valor_f:.2f}')
elif cond == 3:
    valor_f = normal_price
    print(f'Pagamento: 2 Parcelas de R${valor_f/2}')
elif cond == 4:
    valor_f = normal_price + (normal_price*0.2)
    print(f'Pagamento: 3 Parcelas de {valor_f/3}')
print(f'Valor total: R${valor_f:.2f}')