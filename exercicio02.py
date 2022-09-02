# Escreva um programa que faça a leitura das notas dos 3 checkpoints de 15 alunos e mostre a média dos checkpoints para
# cada aluno.

for media in range(1, 16):
    nota1 = float(input('Digite a nota do checkpoint 1: '))
    nota2 = float(input('Digite a nota do checkpoint 2: '))
    nota3 = float(input('Digite a nota do checkpoint 3: '))
    print(f'A média doa aluno {media} é: {(nota1+nota2+nota3)/3:.2f}')
