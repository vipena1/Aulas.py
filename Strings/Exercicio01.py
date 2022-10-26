""" Escreva um programa em Python que, considerando uma string digitada pelo usuário, converta-a em letras minúsculas
e, em seguida, exiba os caracteres na vertical (um debaixo do outro) """

texto = input("Digite algo: ")

print(texto.lower())

for letra in texto:
    print(letra)