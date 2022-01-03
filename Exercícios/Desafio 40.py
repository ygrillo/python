'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
média atingida.
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7 ou superior: Aprovado.
'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1+n2)/2

if m < 5.0:
    print('\033[1;31;40mREPROVADO\033[m')
elif m > 5.0 and m < 7:
    print('\033[1;33;40mRECUPERAÇÃO\033[m')
else:
    print('\033[4;32;mAPROVADO!\033[m \033[32mPARABÉNS')