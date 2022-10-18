"""Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre:
(a) o maior elemento da matriz e sua respectiva posição (linha e coluna);
(b) o menor elemento da matriz e sua respectiva posição."""

matriz = []

for lin in range (0, 6):
    linha = []

    for col in range (0, 3):
        num = int(input("Digite um elemento: "))
        linha.append(num)

    matriz.append(linha)

maior = matriz[0][0]
menor = matriz[0][0]
lin_maior = 0
col_maior = 0
lin_menor = 0
col_menor = 0

'''for lin in range (0, 6):
    for col in range (0, 3):
        if'''
