#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

meters = float(input('Metros: '))

cent = meters*100
mili = meters*1000

print(f'Centímetros: {cent:.0f}\nMilímetros: {mili:.0f}')