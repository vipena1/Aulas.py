""" Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de
dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados,
faça: Mostre a quantidade de valores que foram lidos;

a. Calcule e mostre a soma dos valores;

b. Calcule e mostre a média dos valores;

c. Calcule e mostre a quantidade de valores acima da média calculada;

d. Calcule e mostre a quantidade de valores abaixo de sete."""

listaNotas = []

soma = 0
valorAcima = 0
valorAbaixo = 0


nota = float(input("Digite uma nota: "))
while nota != 0:
    listaNotas.append(nota)
    nota = float(input("Digite uma nota: "))

tam = len(listaNotas)

for i in range(0, tam):
    soma = soma + listaNotas[i]
    if listaNotas[i] < 7.0:
        valorAbaixo = valorAbaixo + 1

media = soma / tam

for i in range(0, tam):
    if listaNotas[i] > media:
        valorAcima = valorAcima + 1

print(f"A soma dos valores é: {soma}")
print(f"A média dos valores é: {media}")
print(f"A quantidade de valores acima da média é: {valorAcima}")
print(f"A quantidade de valores abaixo da média é: {valorAbaixo}")
