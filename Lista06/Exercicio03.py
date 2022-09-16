# Escreva um programa que pergunte em qual mês estamos (1-12) e ao final utilize uma estrutura de decisão por seleção
# para escrever o nome do mês por extenso na tela.

mes = int(input('Insira o mês atual: '))

if mes == 1:
    print('JANEIRO')

elif mes == 2:
    print('FEVEREIRO')

elif mes == 3:
    print('MARÇO')

elif mes == 4:
    print('ABRIL')

elif mes == 5:
    print('MAIO')

elif mes == 6:
    print('JUNHO')

elif mes == 7:
    print('JULHO')

elif mes == 8:
    print('AGOSTO')

elif mes == 9:
    print('SETEMBRO')

elif mes == 10:
    print('OUTUBRO')

elif mes == 11:
    print('NOVEMBRO')

elif mes == 12:
    print('DEZEMBRO')

else:
    print('Insira um mês valido.')

