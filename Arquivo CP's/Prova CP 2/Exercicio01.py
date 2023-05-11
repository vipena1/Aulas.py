valor = float(input("Digite o valor do produto: R$"))

valorTotal = 0

while valor > 0:
    quantidade = int(input("Digite a quantidade de produtos: "))

    valorTotal = valorTotal + (valor * quantidade)

    valor = float(input("Digite o valor do produto: R$"))

print(f"O valor a ser pago é de : R${valorTotal}")