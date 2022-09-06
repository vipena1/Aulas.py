# Com a volta das aulas presenciais, a mãe de um aluno do ensino fundamental necessita saber quanto gastará
# com material escolar. Para fazer uma simulação, ela foi a uma livraria com o objetivo de simular a compra dos
# seguintes itens básicos: canetas, lápis e cadernos.
# Um ponto a se considerar é que essa livraria está com um programa de desconto de 20% nos preços dos cadernos
# e 5% nas canetas. Assim sendo, escreva um programa em Python que solicite as quantidades dos itens,
# preços e calcule o total da compra simulada.

precoCaneta = float(input('Digite o preço de cada caneta: R$'))
qtdCaneta = int(input('Digite a quantidade de canetas que deseja comprar: '))
precoLapis = float(input('Digite o preço de cada lápis: R$'))
qtdLapis = int(input('Digite a quantidade de lápis que deseja comprar: '))
precoCadernos = float(input('Digite o preço de cada caderno: R$'))
qtdCaderno = int(input('Digite a quantidade de cadernos que deseja comprar: '))

totalCaneta = (precoCaneta * qtdCaneta) - 0.05 * (precoCaneta * qtdCaneta)
totalLapis = precoLapis * qtdLapis
totalCaderno = (precoCadernos * qtdCaderno) - 0.20 * (precoCadernos * qtdCaderno)

print(f'''O valor total da compra é de R${totalLapis+totalCaneta+totalCaderno} sendo gasto o seguinte com cada item:
Caneta R${totalCaneta:.2f}
Lápis R$ {totalLapis:.2f}
Caderno R$ {totalCaderno:.2f}
''')
