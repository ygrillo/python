#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes a letra 'a' aparece.
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

frase = input('Frase: ')    #frase recebe a frase do usuário

vezes_a = frase.count('a')  #Conta quantas vezes a letra 'a' aparece
pos1_a = frase.find('a')    #Mostra em que posição a letra 'a' aparece pela primeira vez
pos2_a = frase.rfind('a')   #Mostra em que posição a letra 'a' aparece pela última vez

print(f'Vezes: {vezes_a}\nPrimeira posição: {pos1_a}\nÚltima posição: {pos2_a}')