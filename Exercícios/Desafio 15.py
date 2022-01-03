# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmp = int(input('Km Rodados: '))
dias = int(input('Tempo de locação: '))

pf = (60 * dias) + (0.15 * kmp)

print(f'Preço final: R${pf:.2f}')
