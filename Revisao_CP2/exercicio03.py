"""Escreva um programa em Python que solicite 10 números inteiros ao usuário e que, ao final, mostre qual é
 o maior número. Utilize a estrutura de repetição “for”."""
print("Digite 10 números para verificação de qual o maior.")

maiorNumero = 0

for n in range(1, 11):
    numero = int(input(f"Digite o {n}° número: "))

    if numero > maiorNumero:
        maiorNumero = numero


print(maiorNumero)
