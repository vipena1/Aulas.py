# uma função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá
# solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função
# valorPagamento. O cálculo do valor a ser pago é feito da seguinte forma: para pagamentos sem atraso, cobrar o valor
# da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

valPrestacao = float(input("Digite"))
diasAtraso = float(input("Digite"))


def valorPagamento(valPrestacao, diasAtraso):
    if diasAtraso > 0:
        return (valPrestacao * 0.03) + valPrestacao + ((0.001 * diasAtraso) * valPrestacao)

    else:
        return valPrestacao


print(valorPagamento(valPrestacao, diasAtraso))
