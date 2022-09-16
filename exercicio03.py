# Escreva um programa que calcule a soma de todos os números pares entre 1 e 20.

soma = 0

for num in range(1, 21):
    if num% 2 == 0:
        soma = soma + num

print(f'A soma dos números pares entre 1 e 20 é: {soma}')


