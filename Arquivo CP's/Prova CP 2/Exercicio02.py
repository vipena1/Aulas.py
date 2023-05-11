cont = 0

for n in range(0, 10):
    numero = int(input("Digite um número: "))

    if numero < 0:
        cont = cont + 1

print(f"A quantidade de números negativos é: {cont}")
