"""Faça um programa em Python que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos,
 cujos valores deverão ser compostos pelos elementos intercalados das 2 listas."""

listaUm = []
listaDois = []
listaInter = []
soma = 0

for i in range(1, 11):
    numListaUm = int(input(f"Digite o {i}° número da lista 1: "))
    listaUm.append(numListaUm)
    listaInter.append(numListaUm)

    numListaDois = int(input(f"Digite o {i}° número da lista 2: "))
    listaDois.append(numListaDois)
    listaInter.append(numListaDois)
    
print(listaUm)
print(listaDois)
print(listaInter)
