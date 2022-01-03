#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex.: Ana Maria de Souza
#Primeiro: Ana
#Último: Souza

nome = input('Nome completo: ') #var nome recebe o nome da pessoa

divide = nome.split()   #Cria uma lista com cada palavra do nome

p_nome = divide[0].strip()  #Mostra o primeiro nome e elimina espaços desnecessários
tamanho = len(divide)   #Calcula quantas palavras tem dentro de divide
u_nome = divide[tamanho-1].strip()  #Mostra o último nome e elimina espaços desnecessários

if u_nome == p_nome:
    u_nome = 'Não tem'

print(f'Primeiro: {p_nome}\nÚltimo: {u_nome}')
print(f'Formal: {u_nome}, {p_nome}')