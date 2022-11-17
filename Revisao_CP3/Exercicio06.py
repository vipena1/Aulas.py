""" Escreva um programa em Python para ler uma matriz 3X6 de números reais. Em seguida, quando houver números
negativos, troque-os pelo número 1. Por fim, mostre a matriz atualizada. """

matriz = []

for lin in range(0, 3):
    linha = []
    for col in range(0, 9):
        linha.append(int(input("Digite o elemento da matriz: ")))
    matriz.append(linha)

for lin in range(0, 3):
    for col in range(0, 6):
        if (matriz[lin][col] < 0):
            matriz[lin][col] = 1

'''for i in range(0, 3):'''
