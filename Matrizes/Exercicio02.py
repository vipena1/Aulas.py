"""Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos
da diagonal principal da matriz por um número k. Imprima a matriz na tela antes e
depois da multiplicação"""

matriz = []
mult = int(input("Digite um número para multiplicar os números da matriz na giagonal: "))

for i in range(1, 4):
    lista = []

    for j in range(1, 4):
        num = int(input(f"Digite o {j}° número da {i}° lista: "))
        '''if (i == 1 and j == 1) or (i == 2 and j == 2) or (i == 3 and j == 3):
            num = num * mult'''
        lista.append(num)

    matriz.append(lista)


print(matriz)
'''conta = matriz[0][0]*mult, matriz[1][1]*mult, matriz[2][2]*mult
matriz.append(conta)

print(matriz)'''

