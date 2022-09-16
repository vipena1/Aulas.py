"""Escreva um algoritmo que solicite dois números e devolva quantos pares e
ímpares há entre esses dois números. Exemplo: entre 7 e 10 há 2 números
pares e 2 números ímpares
"""

numUm = int(input("Digite o primeiro número: "))
numDois = int(input("Digite o segundo número: "))

i = numUm
impar = 0
par = 0

while i <= numDois:
    if i%2 == 0:
        par = par+1

    else:
        impar = impar + 1

    i = i + 1

print(f"Entre {numUm} e {numDois} há {par} números pares e {impar} números ímpares.")
