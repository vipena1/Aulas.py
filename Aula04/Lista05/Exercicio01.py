# Um condomínio possui 4 blocos que são abastecidos por duas caixas d’água diferentes.
# A caixa A abastece os blocos pares e a caixa B abastece os blocos ímpares.
# Escreva um algoritmo que pergunte ao usuário em qual bloco ele mora (1-4)
# e escreva na tela qual a caixa que abastece seu bloco: a caixa a ou a caixa B;

bloco = int(input('Insira o número do bloco que você mora: '))

if bloco == 2 or bloco == 4:
    print('Seu bloco é abastecido pela caixa A.')

elif bloco == 1 or bloco == 3:
    print('Seu bloco é abastecido pela caixa B.')

else:
    print('Insira um bloco valido.')
