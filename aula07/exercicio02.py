# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12.
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

qtdMacas = int(input('Quantas maçâs foram comprasdas? '))

if 0 < qtdMacas < 12:
    print(f'O total da sua compra foi de R${qtdMacas*1.30}.')

elif qtdMacas > 12:
    print(f'O total da sua compra foi de R${qtdMacas*1}.')

else:
    print('Insira um valor valido para o calculo.')
    