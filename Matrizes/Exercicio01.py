"""Escreva um programa que leia uma matriz 4 x 4, conte e escreva quantos valores
maiores que 10 ela possui."""

soma = 0
matriz = []

for j in range(1, 5):
    lista = []

    for i in range(1, 5):

        num = float(input(f"Digite o {i}° número da {j}° lista: "))
        lista.append(num)
        if num > 10:
            soma = soma + 1

    matriz.append(lista)

print(f"Existem {soma} números maiores que 10.")
print(matriz)

