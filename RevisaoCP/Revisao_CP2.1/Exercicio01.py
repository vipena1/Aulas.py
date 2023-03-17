"""Escreva um programa em Python (estrutura “main”) que contenha as seguintes funções:

a) Uma função que receba como parâmetro um número n e exiba todos os pares de 1 a n;

b) Uma função que receba como parâmetro um número n e verifique e retorne o fatorial desse número.

c) Uma função que receba como parâmetro um número n e exiba a tabuada desse número."""

def main():
    n = int(input("Difite um número: "))
    allPares(n)
    fatorial(n)

def allPares(n):
    for i in range (1, n+1):
        if i % 2 == 0:
            print(i)

def fatorial(n):
    if n > 0:
        for i in range (1, n):
            n = n * i

        print(n)

if __name__ == '__main__':
    main()