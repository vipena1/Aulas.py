# uma função chamada somaImposto, que possua dois parâmetros: taxaImposto, que é a quantia de imposto sobre vendas
# expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para
# incluir o imposto sobre vendas.

valor = float(input("Digite o valor valor do item: "))
taxa = float(input("Digite a porcentagem de imposto: "))


def somaImposto(taxaImposto, custo):
    return custo + (custo*(taxa/100))


print(somaImposto(taxa, valor))