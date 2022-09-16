""" Somar todos os números inteiros de 1 a N, em que N é um número inteiro
digitado pelo usuário. Exemplo: usuário digita o valor de N igual a 5, então
soma = 1 + 2 + 3 + 4 + 5 = 15. """

num = int(input("Digite um número para saber a soma de 0 até ele: "))

cont = 1
soma = 0

while cont <= num:
    soma = soma + cont
    cont = cont + 1

print(f"A soma de 0 até {num} é igual {soma}.")
