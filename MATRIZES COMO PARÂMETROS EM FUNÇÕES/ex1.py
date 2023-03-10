"""Escreva um programa em Python (estrutura “main”) que contenha as seguintes funções:

· Uma função para carregar uma matriz 3x4 de números inteiros com a matriz sendo um parâmetro;

· Uma função para exibir os elementos da matriz 3x4 com a matriz sendo um parâmetro;

· Uma função que calcule e retorne a quantidade de números pares e ímpares contidos na matriz 3x4, a qual deve
ser um parâmetro."""


def main():
    matriz = []
    carrega_matriz(matriz, 3, 4)
    exibe_matriz(matriz, 3)
    cont_par, cont_impar = conta_pares_impares (matriz, 3, 4)
    print("Quantidade de pares na matriz: ", cont_par)
    print("Quantidade de impares na matriz: ", cont_impar)


def carrega_matriz(matriz, nlin, ncol):
    for lin in range (0, nlin):
        linha = []

        for col in range (0, ncol):
            linha.append(int(input("Digite um elemento: ")))
        matriz.append(linha)

def exibe_matriz (matriz, nlin):
    for lin in range (0, nlin):
        print(matriz[lin])


def conta_pares_impares (matriz, nlin, ncol):
    cont_par = 0
    cont_impar = 0
    for lin in range (0, nlin):
        for col in range (0, ncol):
            if (matriz[lin][col]% 2 == 0):
                cont_par += 1

            else:
                cont_impar += 1

    return (cont_par, cont_impar)

if (__name__ == "__main__"):
    main()
