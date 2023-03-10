"""Escreva um programa em Python (estrutura “main”) que contenha as seguintes funções:

· Uma função para carregar uma matriz 3x3 de números inteiros com a matriz sendo um parâmetro;

· Uma função para exibir os elementos da matriz 3x3 com a matriz sendo um parâmetro;

· Uma função que calcule e retorne a soma dos elementos da diagonal principal da matriz 3x3, a qual deve ser
um parâmetro."""

def main():
    matriz = []
    carrega_matriz(matriz, 3, 3)
    exibe_matriz(matriz, 3)
    print ("Soma da diagonal: ", soma_diagonal(matriz, 3, 3))



def carrega_matriz(matriz, nlin, ncol):
    for lin in range (0, nlin):
        linha = []

        for col in range (0, ncol):
            linha.append(int(input("Digite um elemento: ")))
        matriz.append(linha)

def exibe_matriz (matriz, nlin):
    for lin in range (0, nlin):
        print(matriz[lin])


def soma_diagonal (matriz, nlin, ncol):
    soma = 0
    for lin in range (0, nlin):
        for col in range (0, ncol):
            if (lin == col):
                soma += matriz[lin][col]

    return soma

if (__name__ == "__main__"):
    main()