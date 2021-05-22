def ordenar(lista):
    for i in range(0, len(lista) - 1):
        for cont in range(i+1, len(lista)):
            if lista[i] > lista[cont]:
                troca = lista[i]
                lista[i] = lista[cont]
                lista[cont] = troca
    return lista