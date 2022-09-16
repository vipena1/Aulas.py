# Um estacionamento cobra R$ 5,00 por hora porém possui um teto de cobrança máxima de R$ 35,00,
# independente do número de horas. Escreva um algoritmo que pergunte ao usuário qual foi o período de
# permanência em horas e escreva na tela o total a pagar.

horas = float(input('Insira quantas horas permaneceu no estacionamento: '))
pagar = horas*5

if pagar <= 35:
    print(f'O valor a ser pago é R${pagar:.2f}')

else:
    print('O valor a ser pago é R$35.00 ')

