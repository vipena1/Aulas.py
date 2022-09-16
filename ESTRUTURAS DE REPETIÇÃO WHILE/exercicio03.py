"""Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem ser somados.
Escreva o valor final da soma efetuada. """

num = int(input("Digite um número: "))

cont = 1
soma = num

while num < 40 and cont < 10:
    soma = soma + num
    cont = cont + 1
    num = int(input("Digite outro número: "))

print(f"A soma dos valores é: {soma}")