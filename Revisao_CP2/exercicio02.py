

dentro = 0
fora = 0

for n in range(0, 10):

    valor = int(input("Digite um valor: "))

    if 10 <= valor <= 20:
        dentro = dentro + 1

    else:
        fora = fora + 1


print(f"Quantidade numeros entre 10 e 20 é :{dentro}, e a quantidade fora é :{fora}")

