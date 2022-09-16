# Um condomínio possui 20 blocos e para uma correta administração possui dois síndicos:
# o sr José que administra os blocos de 1 a 10 e o sr Hamilton que administra os blocos de 11 a 20.
# Escreva um algoritmo que pergunte ao usuário em qual bloco ele mora e escreva na tela qual o síndico responsável;

bloco = int(input('Insira o número do bloco que você mora: '))

if 1 <= bloco <= 10:
    print('Seu síndico é o José.')

elif 11 <= bloco <=20:
    print('Seu síndico é o Hamilton.')

else:
    print('Insira um bloco valido.')