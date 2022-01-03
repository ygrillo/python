#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em Celsius: '))

fah = celsius * 1.8 + 32

print(f'Temperatura em Fahrenheit: {fah:.1f} ºF')