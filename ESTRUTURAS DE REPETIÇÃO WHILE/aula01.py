#Criando uma tabuada com estruturas de repetição.

numero = int(input("Digite o número em que deseja ver a tabuada: "))

i = 1

while i <= 10:
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")
    i = i + 1

