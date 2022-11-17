""" Crie um programa em Python com o menu abaixo para realizar as operações (CRUD) em uma lista de clientes 
(dicionário de dicionários) de uma determinada loja. 

1-Incluir 
2-Alterar 
3-Exibir
4-Excluir

Os dados a serem armazenados devem ser os seguintes: nome, CPF, idade, endereço e limite de crédito. Na opção de 
alteração dos dados, permita que o usuário altere todos os campos, exceto o nome. As operações deverão ser executadas 
até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). Quando o usuário não desejar mais 
efetuar as operações, faça um relatório de todos os clientes cujo limite de crédito é maior do que 1500,00. """

resp = 1
usuario = {}

while (resp == 1):
    print("1-Incluir ")
    print("2-Alterar ")
    print("3-Exibir ")
    print("4-Excluir ")
    opc = int(input("Digite a opção desejada: "))

    if (opc == 1):
        nome = input("Nome: ").upper()
        cpf = int(input("CPF: "))
        idade = int(input("Idade: "))
        endereco = input("Endereço: ").upper()
        lim_credito = float(input("Limite de crédito: "))
        usuario[nome] = {"Nome": nome, "CPF": cpf, "Idade": idade, "Endereço": endereco, "Limite de crédito": lim_credito}

    elif (opc == 2):
        nome = input("Digite o nome para busca: ").upper()

        if (nome in usuario):
            usuario[nome]["CPF"] = int(input("CPF: "))
            usuario[nome]["Idade"] = int(input("Idade: "))
            usuario[nome]["Endereço"] = input("Endereço: ")
            usuario[nome]["Limite de crédito"] = float(input("Limite de crédito: "))

        else:
            print("Usuario não encontrado!")

    elif (opc == 3):
        nome = input("Digite o nome para busca: ").upper()

        if (nome in usuario):
            print(usuario[nome])

        else:
            print("Usuario não encontrado")

    elif (opc == 4):
        nome = input("Digite o nome para excluir: ").upper()

        if (nome in usuario):
            del usuario[nome]

        else:
            print("Usuario não encontrado!")

    resp = input("Deseja continuar? (1-SIM / 0-NÃO): ")

'''lim_maior = []

if usuario[nome]["Limite de crédito"] >= 1500:'''
