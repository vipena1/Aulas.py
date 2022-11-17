""" Elaborar um programa em Python que efetue o cálculo de uma tabuada de um número qualquer e armazene os resultados
em uma lista A para 11 elementos. Apresentar os valores armazenados na lista """

lista = []
num_tabuada = int(input("Digite o número da tabuada que deseja: "))

for i in range(0, 11):
    lista.append(num_tabuada*i)

print(lista)