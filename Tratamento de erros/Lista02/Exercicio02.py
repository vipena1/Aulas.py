""" Escreva um programa em Python que faça um CRUD em um dicionário de dicionários, os quais devem conter os
seguintes dados:

a. Código

b. Descrição do produto

c. Quantidade em estoque

d. Valor do produto

Faça o tratamento de erros no processo de inserção e alteração. As operações deverão ser executadas até que o
usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO)."""


produtos = {}
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
            descr = input("Digite o nome do funcionario: ")
            qntd = int(input("Digite a idade do funcionairo: "))
            valor = float(input("Digite o salario do funcionario: "))
        except ValueError:
            print("Digte um valor numerio! ")
        else:
            produtos[cod] = {'codigo': cod, 'descrição': descr, 'qntd': qntd, 'valor': valor}
        finally:
            print("Operação finalizada")

    elif opc == 2:
        try:
            cod = int(input("Digite o codigo do produto a ser alterado: "))
        except ValueError:
            print("Digte um valor numerio! ")
        else:
            if cod in produtos:
                try:
                    descr = input("Digite o nome do funcionario: ")
                    qntd = int(input("Digite a idade do funcionairo: "))
                    valor = float(input("Digite o salario do funcionario: "))
                except ValueError:                    \
                    print("Digte um valor numerio! ")
                else:
                    funcionarios[cod]['descriçaõ']=descr
                    funcionarios[cod]['qntd']=qntd
                    funcionarios[cod]['valor']=valor

                finally:
                    print("Operação finalizada!")
            else:
                print("Codigo invalido!")

        finally:
            print("Operação finalizada")

    elif opc == 3:
        cod = int(input("Digite o codigo do produtos a ser excluido"))
        if cod in produtos:
            del produtos[cod]

        else:
            print("Codigo invalido")

    elif opc == 4:
        print(produtos)

    else:
        print("Operação finalizada")

    resp = input("Digite S/N")
