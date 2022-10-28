""" Escreva um programa em Python que crie uma lista de 10 funcionários, utilizando o conceito de dicionários,
contendo os seguintes dados:
§ Nome;
§ Cargo;
§ Salário.

Depois da lista criada, faça a busca pelo nome de um funcionário qualquer e mostre seus dados."""

funcionario = {}

for i in range(0, 2):
    nome = input("Nome: ").upper()
    cargo = input("Cargo: ").upper()
    salario = float(input("Salário: "))
    funcionario[nome] = {"Nome": nome, "Cargo": cargo, "Salário": salario}

print(funcionario)
print("\n")

nome = input("Digite um nome a ser procurado: ").upper()

if (nome in funcionario):
    print(funcionario[nome])
else:
    print("Funcionario não encontrado")


