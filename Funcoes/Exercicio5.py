# Uma função que carregue uma lista com 10 elementos e, em seguida, outra função que retorne o maior elemento dessa lista.

lista = []


def listaElementos(listaElemento):
    for i in range(0, 10):
        listaElemento.append(float(input("Digite um número :")))

    return listaElemento


def maiorElemento(maior):
    maior = lista[0]
    for i in range(1, 10):
        if lista[i] > maior:
            maior = lista[i]

    return maior


print(listaElementos(lista))
print(maiorElemento(lista))
