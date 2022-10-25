"""Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre:
(a) o maior elemento da matriz e sua respectiva posição (linha e coluna);
(b) o menor elemento da matriz e sua respectiva posição."""

matriz = []
lin_maior = 0
col_maior = 0
lin_menor = 0
col_menor = 0

for lin in range(0, 6):
    linha = []
    for col in range(0, 3):
        num = float(input("Digite um elemento da matriz: "))
        linha.append(num)
    matriz.append(linha)

for lin in range (0,6):
    if (lin==0):
        maior = matriz[0][0]
        menor = matriz[0][0]
    for col in range (0,3):
            if (matriz[lin][col] > maior):
                maior = matriz[lin][col]
                lin_maior = lin
                col_maior = col
            if (matriz[lin][col] < menor):
                menor = matriz[lin][col]
                lin_menor = lin
                col_menor = col

print(matriz)
print(f"Maior elemento: {maior:.2f}")
print("O maior elemento está na linha ", lin_maior, " e coluna ", col_maior)
print("O menor elemento está na linha ", lin_menor, " e coluna ", col_menor)
print(f"Menor elemento: {menor:.2f}")