'''Faça um programa em Python que leia 10 números inteiros e armazene-os em uma lista. Em seguida, armazene os
números pares na lista PAR e os números ÍMPARES na lista ímpar. Por fim, imprima as 3 listas '''

lista = []
listaPar = []
listaImpar = []
for i in range (1, 11):
    num = int(input(f"Digite o {i}° número da lista: "))
    lista.append(num)
    if num % 2 == 0:
        listaPar.append(num)

    else:
        listaImpar.append(num)

print(lista)
print(listaPar)
print(listaImpar)
