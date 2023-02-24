"""
Autor: Vinicius Pena
Programa: Exercicio Python
Aula: Função
Data: 23/02/2023
Descrição: Faça uma função comum que calcule 20% de desconto para a próxima black Friday. Utilize-a numa lista que tem
os preços dos itens que você planeja comprar. Faça isso primeiro sem MAP e depois com MAP. OBS: o programa deve ter,
obrigatoriamente, a função “main”. """

" Sem a função MAP. "


def main():
    lista_preco = [100, 50, 75, 200, 150]  # lista de preços dos itens a comprar
    print("***FUNÇÃO SEM O USO DO MAP***")
    lista_desconto = calcular_desconto(lista_preco)
    print(lista_desconto)

    print("***FUNÇÃO COM O USO DO MAP***")
    lista_desconto = list(map(calcular_desconto_simples, lista_preco))
    print(lista_desconto)


def calcular_desconto(preco):
    lista_descontos = []

    # aplicando desconto de 20% em cada preço e adicionando à lista de preços descontados

    for i in range(0,len(preco)):
        lista_descontos.append(preco[i] * 0.80)

    return lista_descontos


def calcular_desconto_simples(preco):

    # aplicando desconto com MAP
    preco_desconto = preco*0.80
    return preco_desconto


if (__name__ == "__main__"):
    main()