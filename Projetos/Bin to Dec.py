def bintodec(bin: str):
    
    bin_dec = str(bin)

    # populo a lista
    lista = [x for x in bin_dec]

    # inverto a ordem
    lista = lista[::-1]

    # para inteiro
    lista = [int(x) for x in lista]

    lista_dec = []

    for x in range(len(lista)):
        y = lista[x] * (2 ** x)
        lista_dec.append(y)
    
    # faço a soma
    return sum(lista_dec)
    

def dec_to_bin(dec: int):
    lista = []
    while dec // 2 > 1:
        lista.append(dec % 2)
        dec = dec // 2
    if dec % 2 == 1:
        prefix = 11
    else:
        prefix = 10

    print(str(prefix) + ''.join([str(x) for x in lista[::-1]]))


dec_to_bin(23)