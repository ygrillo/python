def bin_to_dec(bin: str):
    
    bin_dec = str(bin)

    # populo a lista, transformo em inteiro e inverto a ordem
    lista = [int(x) for x in bin_dec][::-1]

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

    return str(prefix) + ''.join([str(x) for x in lista[::-1]])


print(dec_to_bin(10))
print(bin_to_dec("1001"))