import sys


def main():
    if (len(sys.argv)==3):
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print("Soma: ", somaNumeros(x, y))

    else:
        print("Número de argumentos invalido!")


def somaNumeros(x, y):
    soma = x + y
    return (soma)


if (__name__ == "__main__"):
    main()