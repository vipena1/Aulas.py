# Escreva um programa que leia um ano qualquer e verifique se o mesmo está entre 1000 e 2999, caso não esteja
# apresentar uma mensagem de erro. Caso esteja nessa faixa verificar se o ano é bissexto. Um ano é bissexto caso seja
# divisível por 4 mas não por 100. Um ano também é bissexto se for divisível por 400.

ano = int(input('Digite o ano desejado para verificar se ele é bissexto: '))

bissexto = ano % 4

if 1000 <= ano <= 2999:

    if bissexto == 0:
        print(f'O ano {ano} é bissexto!')
    else:
        print(f'O ano {ano} não é bissexto.')

else:
    print('ERRO')
