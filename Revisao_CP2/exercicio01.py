cod = int(input("""Para adicionar um produto, digite o código e para finalizar a conta digite "0".
Digite o código do produto que deseja adicionar: """))

soma = 0
while ( cod > 0):
    if cod == 1:
        soma = soma + 35

    elif cod == 2:
        soma = soma + 25

    elif cod == 3:
        soma = soma + 40

    elif cod == 4:
        soma = soma + 55

    elif cod == 5:
        soma = soma + 18

    else:
        print("Digite um código válido")

    cod = int(input("Digite o código do produto que deseja adicionar: "))


print(soma)