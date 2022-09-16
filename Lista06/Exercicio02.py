# Escreva um programa que pergunte as medidas dos três lados de um triângulo e diga que o mesmo é isósceles,
# equilátero ou escaleno.
# Isósceles = Dois dos três lados iguais.
# equilátero = Três lados iguais.
# escaleno = Três lados diferentes.

ladoUm = float(input('Insira o primeiro lado do triângulo: '))
ladoDois = float(input('Insira o segundo lado do triângulo: '))
ladoTres = float(input('Insira o treceiro lado do triângulo: '))

if (ladoUm == ladoDois and ladoUm != ladoTres) or (ladoUm == ladoTres and ladoUm != ladoDois) or (ladoDois == ladoTres and ladoDois != ladoUm):
    print('O triângulo é um Isósceles.')

elif ladoUm == ladoDois == ladoTres:
    print('O triângulo é um equilátero.')

elif ladoUm != ladoDois != ladoTres:
    print('O triângulo é um escaleno.')