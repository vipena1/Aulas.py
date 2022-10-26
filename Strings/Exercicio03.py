""" Um palíndromo é um tipo de palavra ou frase que tem a propriedade de ser lida tanto da direita para a esquerda
quanto da esquerda para a direita. Como exemplo, temos a palavra “asa”. Baseado nesse conceito, escreva um programa
em Python que, dada uma palavra, verifique se ele é um palíndromo ou não. DICA: utiliza a notação de slice. """

texto = input("Digite algo: ")
palavra = texto.split()
junto = "".join(palavra)
inverso = ""

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

if junto == inverso:
    print("O texto é um palíndromo! ")

else:
    print("O texto não é um palíndromo! ")
