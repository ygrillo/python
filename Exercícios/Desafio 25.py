#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

nome = input('Digite seu nome: ')   #nome recebe o nome da pessoa

lista = nome.split()    #Transforma o nome em uma lista de palavras

question = 'Silva' in lista #Pergunta se existe 'Silva' na lista

if question == True:
    print('Você tem "Silva" no seu nome')
else:
    print('Você não tem "Silva" no seu nome')