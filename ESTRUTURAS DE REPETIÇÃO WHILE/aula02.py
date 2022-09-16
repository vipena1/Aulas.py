# Criando uma soma de numeros inteiros

num = int(input("Digite um número inteiro para somar, para finalizar a soma digite 0: "))

soma = 0

while num > 0:
    soma = soma + num
    num = int(input("Digite um número inteiro para somar, para finalizar a soma digite 0: "))

print(f"A soma total é {soma}")