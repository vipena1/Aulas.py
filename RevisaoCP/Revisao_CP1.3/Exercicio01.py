""" Escreva um programa em Python para ler uma lista A com 10 elementos numéricos inteiros. Apresentar o total de 
elementos ímpares existentes na lista e o percentual do valor total de números ímpares em relação à quantidade total 
de elementos armazenados na lista. """

lista = []
qtde_impares = 0

for i in range (0, 10):
    lista.append(int(input("Digite um elemento: ")))

for i in range (0, 10):
    if  lista[i] % 2 != 0:
        qtde_impares += 1

percentual_impares = (qtde_impares * 100) / 10

print(qtde_impares)
print(percentual_impares + "%" )