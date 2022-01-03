#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras tem(sem espaços)
#Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')

#Nome com letras maiúsculas e minúsculas

print(nome.upper())
print(nome.lower())

#Quantas letras tem no total(sem espaços)

tira_espaços = nome.strip() #Remove espaços nas laterais
conta_espaço = tira_espaços.count(' ')  #Conta quantos espaços há entre as palavras
print(f'Seu nome possui: {len(tira_espaços)- conta_espaço} caracteres')  #Conta quantos caracteres sobraram, menos o espaço entre as palavras

#Quantas letras tem o primeiro nome

separa = nome.split()   #Separa as palavras do nome
print(separa)   #Mostra como ficou a lista com cada palavra
print(len(separa[0]))   #Conta quantos caracteres tem a primeira palavra que foi separada

