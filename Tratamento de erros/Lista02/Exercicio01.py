"""Escreva um programa em Python que faça um CRUD em um dicionário de dicionários, os quais devem conter os
seguintes dados:

a. Código

b. Nome do funcionário

c. Idade do funcionário

d. Salário do funcionário

Faça o tratamento de erros no processo de inserção e alteração. As operações deverão ser executadas até que o usuário
digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO)."""

funcionarios = {}
resp = "S"
while (resp != "N"):
    print("1 - Inserção")
    print("2 - Alteração")
    print("3 - Remoção")
    print("4 - Exibição")
    opc= int(input("Digite a opção (1-4)"))
    if opc == 1:
        try:
            cod = int(input("Digite o codigo do funcionario: "))
            nome = input("Digite o nome do funcionario: ")
            idade = int(input("Digite a idade do funcionairo: "))
            salario = float(input("Digite o salario do funcionario: "))
        except ValueError:
            print("Digte um valor numerio! ")
        else:
            funcionarios[cod] = {'codigo': cod, 'nome': nome, 'idade': idade, 'salario': salario}
        finally:
            print("Operação finalizada")

    elif opc == 2:
        try:
            cod = int(input("Digite o codigo do funcionario a ser alterado: "))
        except ValueError:
            print("Digte um valor numerio! ")
        else:
            if cod in funcionarios:
                try:
                    nome = input("Digite o nome do funcionario: ")
                    idade = int(input("Digite a idade do funcionairo: "))
                    salario = float(input("Digite o salario do funcionario: "))
                except ValueError:                    \
                    print("Digte um valor numerio! ")
                else:
                    funcionarios[cod]['nome']=nome
                    funcionarios[cod]['idade']=idade
                    funcionarios[cod]['salario']=salario
            else:
                print("Codigo invalido!")

        finally:
            print("Operação finalizada")

    elif opc == 3:
        cod = int(input("Digite o codigo do funcionario a ser excluido"))
        if cod in funcionarios:
            del funcionarios[cod]

        else:
            print("Codigo invalido")

    elif opc == 4:
        print(funcionarios)

    else:
        print("Operação finalizada")

    resp = input("Digite S/N")
