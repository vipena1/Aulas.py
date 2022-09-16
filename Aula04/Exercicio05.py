# Dados 2 números inteiros diferentes digitados pelo usuário, verifique e mostre o
# menor número.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O {num1} é maior que o {num2}.')

elif num1 < num2:
    print(f'O {num2} é maior que o {num1}.')

else:
    print(f'Os valores {num1} e {num2} são iguais. ')