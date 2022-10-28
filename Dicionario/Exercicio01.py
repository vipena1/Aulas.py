""" Escreva um programa em Python que crie uma lista de 15 alunos, utilizando o conceito de dicionários, contendo os
seguintes dados:
§ Nome;
§ Curso;
§ Disciplina;
§ Faltas;
§ 3 checkpoints."""

alunos = {}

for i in range(0, 15):
    nome = str(input("Nome: "))
    disc = input("Disciplina: ")
    curso = input("Curso: ")
    faltas = int(input("Faltas: "))
    checks = []

    for j in range(0, 3):
        checks.append(float(input("Checkpoints: ")))

    alunos[nome] = {
        "nome": nome, "disciplina": disc, "cusro": curso, "faltas": faltas, "checkpoints": checks}

print(alunos)