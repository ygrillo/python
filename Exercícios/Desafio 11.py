# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Largura: '))
alt = float(input('Altura: '))

area = larg * alt
litros = area / 2

print(f'Será(ão) necessário(s) {litros:.2f} litro(s) de tinta')