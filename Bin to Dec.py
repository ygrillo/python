def bintodec(bin):

    lista_bin = []

    binstr = str(bin)

    n = 0

    while n < len(binstr):
        lista_bin.append(binstr[n])
        n += 1

    o = 1
    p = 0
    rf = 0

    while o <= len(binstr):
        x = int(lista_bin[len(lista_bin) - o])  # último caracter da lista
        r = int(x * (2 ** p))
        o += 1
        p += 1
        rf = r + rf

    return rf

print(bintodec(1010))

'''
lista_nome = []

nome = input('Nome: ')
for letras in nome:
    if letras not in ' ':
        lista_nome.append(letras)
print(len(lista_nome))
'''
