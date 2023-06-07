"""NOME E RM DOS INTEGRANTES
JOSÉ CARLOS DA SILVA - RM 97385
LEONARDO GUIMARÃES DE LIMA MARQUES - RM 96409
MARIA LUIZA DE GOVEIA LIMA - RM 97569
MARIANA
VINICIUS DE ABREU PENA - RM 96881"""

import oracledb as orcl
import pandas as pd
from time import sleep
import user
import food
import garden
import plantation

try:
    # Abrindo conexão com o banco
    dnStr = orcl.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = orcl.connect(user="RM96881", password="250998", dsn=dnStr)

    inst_consult = conn.cursor()
    inst_register = conn.cursor()
    inst_update = conn.cursor()
    inst_delete = conn.cursor()
    inst_extract = conn.cursor()  # extrair relatorios

except Exception as e:
    # Se der erro retornara o motivo
    print("Erro: ", e)
    connection = False

else:
    connection = True

while connection:

    try:
        opt = int(input("""\nMENU DE ADMINSTRADOR.
1 - USUÁRIO
2 - ALIMENTO
3 - HORTA
4 - PLANTAÇÃO
5 - RELATORIOS
0 - SAIR
SELECIONE UM NÚMERO PARA REALIZAR ALTERAÇÕES: """))

    except ValueError:
        print("\nDIGITE APENAS VALORES NUMERICOS.")
        sleep(2)

    else:
        # USANDO A ENTIDADE USUARIO
        if opt == 1:
            try:
                opt = int(input("""\n - USUARIO - 
1 - INSERIR
2 - VISUALIZAR
3 - ALTERAR
4 - EXCLUIR
0 - SAIR
DIGITE UMA OPÇÃO: """))
            except ValueError:
                print("\nDIGITE APENAS VALORES NUMERICOS. ")
                sleep(2)

            else:
                # CADASTRANDO UM NOVO USUÁRIO
                if opt == 1:

                    user.insert()

                # LEITURA DOS DADOS DOS USUÁRIOS
                elif opt == 2:

                    user.consult()

                # ALTERANDO OS DADOS DOS USUÁRIOS
                elif opt == 3:

                    user.alter()

                elif opt == 4:

                    user.delete()

                elif opt == 0:
                    print("\nVOLTE SEMPRE!")
                    connection = False

                else:
                    print("\nDIGITE UMA OPÇÃO VÁLIDA")
                    sleep(2)

        # USANDO A ENTIDADE ALIMENTO
        elif opt == 2:
            try:
                opt = int(input("""\n - ALIMENTO -
1 - INSERIR
2 - VISUALIZAR
3 - ALTERAR
4 - EXCLUIR
0 - SAIR
DIGITE UMA OPÇÃO: """))
            except ValueError:
                print("\nDIGITE APENAS VALORES NUMERICOS. ")
                sleep(2)

            else:
                if opt == 1:

                    food.insert()

                elif opt == 2:

                    food.consult()

                elif opt == 3:

                    food.alter()

                elif opt == 4:

                    food.delete()

                elif opt == 0:
                    print("\nVOLTE SEMPRE!")
                    connection = False

                else:
                    print("\nDIGITE UMA OPÇÃO VÁLIDA")
                    sleep(2)

        # USANDO A ENTIDADE HORTA
        elif opt == 3:
            try:
                opt = int(input("""\n - HORTA - 
1 - INSERIR
2 - VISUALIZAR
3 - ALTERAR
4 - EXCLUIR
0 - SAIR
DIGITE UMA OPÇÃO: """))
            except ValueError:
                print("\nDIGITE APENAS VALORES NUMERICOS. ")
                sleep(2)

            else:
                if opt == 1:

                    garden.insert()

                elif opt == 2:

                    garden.consult()

                elif opt == 3:

                    garden.alter()

                elif opt == 4:

                    garden.delete()

                elif opt == 0:
                    print("\nVOLTE SEMPRE!")
                    connection = False

                else:
                    print("\nDIGITE UMA OPÇÃO VÁLIDA")
                    sleep(2)

        # USANDO A ENTIDADE PLANTAÇÃO
        elif opt == 4:
            try:
                opt = int(input("""\n - PLANTAÇÃO - 
1 - INSERIR
2 - VISUALIZAR
3 - ALTERAR
4 - EXCLUIR
0 - SAIR
DIGITE UMA OPÇÃO: """))
            except ValueError:
                print("\nDIGITE APENAS VALORES NUMERICOS. ")
                sleep(2)

            else:
                if opt == 1:

                    plantation.insert()

                elif opt == 2:

                    plantation.consult()

                elif opt == 3:

                    plantation.alter()

                elif opt == 4:

                    plantation.delete()

                elif opt == 0:
                    print("\nVOLTE SEMPRE!")
                    connection = False

                else:
                    print("\nDIGITE UMA OPÇÃO VÁLIDA")
                    sleep(2)

        # EXTRAÇÃO DE RELATORIOS
        elif opt == 5:
            opt = int(input(f"""\n - RELATORIOS - 
1 - EXTRAIR RELATORIO POR USUARIO
2 - EXTRAIR RELATORIO POR ALIMENTO
3 - EXTRAIR RELATORIO POR HORTA
0 - SAIR

DIGITE UMA OPÇÃO: """))

            if opt == 1:
                print('USUARIO - HORTA - ALIMENTO - QNTD PLANTADA')

            elif opt == 2:
                print('ALIMENTO - HORTA - FILEIRA - POSIÇÃO - QNTD PLANTADA')

            elif opt == 3:
                print('HORTA - FILEIRA - POSIÇÃO - ALIMENTO')

            elif opt == 0:
                print("\nVOLTE SEMPRE!")
                connection = False

            else:
                print("\nDIGITE UMA OPÇÃO VÁLIDA")
                sleep(2)

        elif opt == 0:
            print("\nVOLTE SEMPRE!")
            connection = False

        else:
            print("\nDIGITE UMA OPÇÃO VÁLIDA")
            sleep(2)
