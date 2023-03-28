

dentro = 0
fora = 0

for n in range(1, 11):

    valor = int(input(f"Digite o {n}° número para conferir: "))

    if 10 <= valor <= 20:
        dentro = dentro + 1

    else:
        fora = fora + 1


print(f"Quantidade numeros entre 10 e 20 é :{dentro}, e a quantidade fora é :{fora}")

