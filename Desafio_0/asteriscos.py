def asteriscos(n):
    lista = []
    for i in range(1, n + 1):
        lista.append("*" * i)
    return lista


n = int(input("Digite um valor: "))

print(f"Lista com asteriscos de 1 a {n}: ")
print(asteriscos(n))
