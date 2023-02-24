def calcula_dobro (x):
    dobro = x * 2
    return (dobro)


lista = [1, 2, 3, 4, 5, 6]
lista_dobro = list(map(calcula_dobro, lista))

print(lista_dobro)