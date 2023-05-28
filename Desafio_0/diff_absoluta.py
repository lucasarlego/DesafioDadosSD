def diff_absoluta(lista):
    lista.sort()

    testeAbsol = list(map(lambda a, b: b - a, lista[:-1], lista[1:]))
    menor = min(testeAbsol)

    par = list(filter(lambda x: x[1] - x[0] == menor, zip(lista[:-1], lista[1:])))

    return par


lista = [3, 8, 50, 5, 1, 18, 12]
print(diff_absoluta(lista))
