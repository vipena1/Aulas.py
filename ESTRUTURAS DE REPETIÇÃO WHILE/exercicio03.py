"""Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem ser somados.
Escreva o valor final da soma efetuada. """

cont = 1
soma = 0

while cont <= 10:
    num = int(input("Digite um número: "))
    if num < 40:
        soma = soma + num
    cont = cont + 1

print(f"A soma dos valores é: {soma}")