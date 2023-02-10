# uma função que necessite de três parâmetros (números reais) e que retorne a soma desses três parâmetros.

def somar(n1, n2, n3):
    return n1 + n2 + n3


num1 = float(input("Digite o primeiro número a ser somado: "))
num2 = float(input("Digite o segundo número a ser somado: "))
num3 = float(input("Digite o terceiro número a ser somado: "))

print(somar(num1, num2, num3))
