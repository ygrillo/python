#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = float(input('Digite um número: '))
doble = num * 2
triple = num * 3
square = num ** (1/2)

print(f'Dobro: {doble}\nTriplo: {triple}\nRaiz Quadradra: {square:.3f}')
