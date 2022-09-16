# Considerando 3 notas de avaliações, calcule a média e mostre se o aluno está
# aprovado ou reprovado. Para tanto, considere a aprovação quando a média for
# maior ou igual a 6,0

av1 = float(input('Insira o valor da nota 1: '))
av2 = float(input('Insira o valor da nota 2: '))
av3 = float(input('Insira o valor da nota 3: '))

med = (av1 + av2 + av3)/3

if 6 <= med <= 10:
    print(f'Aluno aprovado com média {med:.2f}.')

elif med > 10:
    print(f'a média foi {med:.2f}, insira um valor correto.')

else:
    print(f'Aluno reprovado com média {med:.2f}')
