#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

city = input('Digite o nome da cidade: ')

divide = city.split()   #Divide as palavras em novas Strings, criando uma lista
santo = 'Santo' in divide[0]    #Pergunta se existe 'Santo' no primeiro item da lista 'divide'


if santo == True:
    print('Sua cidade começa com "Santo"')

else:
    print('Sua cidade não começa com "Santo"')