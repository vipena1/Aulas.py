""" Faça um programa em Python que peça as 3 notas de 10 alunos, calcule e armazene em uma lista a média de cada
aluno. Em seguida, imprima o número de alunos com média maior ou igual a 7.0. """

listaMedia = []
qntdAprovado = 0

for i in range(1, 11):
    nota1 = float(input(f"Digite a nota 1 do {i}° aluno: "))
    nota2 = float(input(f"Digite a nota 2 do {i}° aluno: "))
    nota3 = float(input(f"Digite a nota 3 do {i}° aluno: "))
    media = (nota1 + nota2 + nota3) / 3
    listaMedia.append(media)

for i in range(0, 10):
    if (listaMedia[i] >= 7.0):
        qntdAprovado = qntdAprovado + 1

print(listaMedia)
print(f"A quantidade de alunos aprovados foi de : {qntdAprovado}")
