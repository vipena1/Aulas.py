# Um grupo de amigos resolveu fazer um happy hour em um bar após o horário de trabalho.
# Na ocasião eles pediram porções de batatas fritas, pastéis e cervejas para acompanhar.
# Escreva um programa em Python que calcule o total do pedido baseado nas quantidades de porções e cervejas
# consumidas tendo como referência a tabela abaixo.
# Além disso, calcule o valor individual da conta de acordo com o número de amigos.

'''
    Fritas = R$35
    Pastéis = R$25
    Cerveja = R$18
'''

fritas = float(35)
pasteis = float(25)
cerveja = float(18)

qtdAmigos = int(input('Digite a quantidade de amigos que foram ao happy hour: '))
qtdFritas = int(input('Digite a quantidade de fritas que foram consumidas: '))
qtdPasteis = int(input('Digite a quantidade de pastéis que foram consumidos: '))
qtdCervejas = int(input('Digite a quantidade de cervejas que foram consumidas: '))

print(f'''
O total do pedido é igual a R$ {(qtdFritas*fritas)+(qtdPasteis*pasteis)+(qtdCervejas*cerveja):.2f} sendo cobrado por produto:
Fritas R${qtdFritas*fritas:.2f}
Pasteis R${qtdPasteis*pasteis:.2f}
Cervejas R${qtdCervejas*cerveja:.2f}

A conta dividida por todos da mesa é igual a R${((qtdFritas*fritas)+(qtdPasteis*pasteis)+(qtdCervejas*cerveja))/qtdAmigos:.2f}

''')
