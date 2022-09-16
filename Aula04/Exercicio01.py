# Dado um número inteiro definido pelo usuário, verifique se ele é par ou ímpar.

num = int(input('Insira um numero inteiro para verificar se ele é impar ou par: '))

resultado = num % 2

if resultado == 0:
    print(f'O número {num} é par!')

else:
    print(f'O número {num} é impar! ')
