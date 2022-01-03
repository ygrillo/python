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
    

print(bintodec(1111))