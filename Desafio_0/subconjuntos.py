def subconjuntos(lista):
    subcon = [[]]

    for i in lista:
        subcon += list(map(lambda conj: conj + [i], subcon))

    return subcon


lista = [1, 2]
print(subconjuntos(lista))
