def main():
    #Chamadas das funções

    exibeMensagem()
    x = 7
    y = 9
    print("Soma = ", somaNumeros(x, y))


def exibeMensagem():
    print("Olá")


def somaNumeros (x, y):
    soma = x + y
    return soma


if (__name__ == "__main__"):

    main()
