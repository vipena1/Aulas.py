"""Faça um programa em Python que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos,
 cujos valores deverão ser compostos pelos elementos intercalados das 2 listas."""

listaUm = []
listaDois = []
listaInter = []
soma = 0

for i in range(1, 11):
    num = float(input(f"Digite o {i}° número da 1° lista: "))
    listaUm.append(num)

for i in range(1, 11):
    num = float(input(f"Digite o {i}° número da 2° lista: "))
    listaDois.append(num)



print(listaUm)
print(listaDois)
print(listaInter)
