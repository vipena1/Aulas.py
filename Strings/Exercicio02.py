""" Dada uma string digitada pelo usuário, crie um programa em Python que faça a contagem de vogais existentes nessa
string """

texto = input("Digite algo: ")
soma = 0

for letra in texto:
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        soma = soma + 1

print(f"No texto {texto} existem {soma} vogais.")