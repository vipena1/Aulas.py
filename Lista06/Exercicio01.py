# Escreva um programa que pergunte ao usuário qual foi a média anual de um aluno e ao final diga se ele está
# aprovado, reprovado ou de exame. Considere que o aluno está aprovado caso a média seja maior ou igual a 6.0; de
# exame com a média entre 3.0 e 5.9 e reprovado com média menor do que 3.0.

media = float(input('Digite a média anual para analise: '))

if 6.0 <= media <= 10:
    print('O aluno está aprovado!')

elif 3.0 <= media <= 5.9:
    print('O aluno está de exame.')

elif 0 <= media <= 2.9:
    print('Aluno reprovado!')

else:
    print('Insira uma média menor que 10 e maior que 0.')
