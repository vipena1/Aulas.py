"""
Autor: Vinicius Pena
Programa: Exercicio Python
Aula: Função
Data: 23/02/2023
Dada as listas abaixo, faça uma função que calcule o preço final de cada item dado os descontos para cada um deles.
OBS: o programa deve ter, obrigatoriamente, a função “main”.

# listaOriginal = [234, 64, 13467, 45.89, 23]

# listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]"""


def main():
    listaOriginal = [300, 250.30, 150, 400.20, 730.10]
    listaDescontos = [0.3, 0.4, 0.08, 0.10, 0.20]

    print("***FUNÇÃO SEM O USO DO MAP***")
    lista_desconto = calcular_preco_final(listaOriginal, listaDescontos)
    print(lista_desconto)

    print("***FUNÇÃO COM O USO DO MAP***")
    lista_desconto = list(map(calcular_preco_final_simples, listaOriginal,listaDescontos))
    print(lista_desconto)


def calcular_preco_final(listaOriginal, listaDescontos):
    precos_finais = []
    for i in range(len(listaOriginal)):
        preco_final = listaOriginal[i] * listaDescontos[i]
        precos_finais.append(preco_final)
    return precos_finais


def calcular_preco_final_simples(listaOriginal, listaDescontos):
    preco_desconto = listaOriginal * listaDescontos
    return preco_desconto


if (__name__ == "__main__"):
    main()