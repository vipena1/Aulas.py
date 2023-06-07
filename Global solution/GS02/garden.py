# Funções para entidade horta

import oracledb as orcl
import oracledb.exceptions
import pandas as pd
from time import sleep

connection = False

try:
    # Abrindo conexão com o banco
    dnStr = orcl.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = orcl.connect(user="RM96881", password="250998", dsn=dnStr)

    inst_consult = conn.cursor()
    inst_register = conn.cursor()
    inst_update = conn.cursor()
    inst_delete = conn.cursor()

except Exception as e:
    # Se der erro retornara o motivo
    print("Erro: ", e)
    connection = False

else:
    connection = True


# FUNÇÃO P/ INSERIR NOVO LANÇAMENTO NA HORTA
def insert():
    try:
        # COLETA DE DADOS DA HORTA
        idGarden = int(input("CODIGO DA HORTA: "))
        name = input("NOME DA HORTA: ")
        storagePlanting = int(input("CAPACIDADE PLANTIO: "))

        # COMANDO P/ REGISTRO NO SQL
        register = f"""INSERT INTO HORTA VALUES ({idGarden}, '{name}',{storagePlanting})"""

        # EXECUÇÃO DO COMANDO
        inst_register.execute(register)
        # COMMIT P/ SALVAR OS DADOS INSERIDOS
        conn.commit()

    except ValueError:
        print("\nDIGITE SOMENTE VALORES NUMÉRICO.")
        sleep(2)

    except oracledb.IntegrityError as e:
        error, = e.args
        if error.code == 1438:
            print("\nLIMITE DE CARACTERES ATINGIDO")
            sleep(2)

        elif error.code == 1:
            print("\nO CODIGO DA HORTA JÁ EXISTE")
            sleep(2)

        else:
            print("\nERRO IntegrityError: ", error.code)
            sleep(2)

    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 12899:
            print("\nLIMITE DE CARACTERES TEXTO ATINGIDO.")
            sleep(2)

    except Exception as e:
        print("\nERRO: ", e)
        sleep(2)

    else:
        print("\nCADASTRO REALIZADO.")
        sleep(2)


# FUNÇÃO P/ LER A TABELA HORTA
def consult():
    try:
        # LISTA DE DADOS VAZIA P/ SER ADICIONADO OS DADOS DE LEITURA
        dataList = []

        # COMANDO P/ CONSULTA NO SQL
        inst_consult.execute("SELECT * FROM HORTA")

        # COMANDO P/BUSCAR OS DADOS
        data = inst_consult.fetchall()

        # LOOP P/ SALVAR OS DADOS DENTRO DA LISTA
        for oneData in data:
            dataList.append(oneData)

        dataList = sorted(dataList)

        dataDf = pd.DataFrame.from_records(dataList,
                                           columns=['ID', 'NOME', 'CAPACIDADE'],
                                           index='ID')

        if dataDf.empty:
            print("\nNÃO HÁ REGISTRO NA TABELA DE HORTAS")
            sleep(2)

        else:
            print(dataDf)
            sleep(2)

    except Exception as e:
        print('\n', e)
        sleep(2)


# FUNÇÃO P/ ALTERAR OS DADOS DE UMA HORTA
def alter():
    try:
        datalist = []

        id = int(input("\nDIGITE O ID DA HORTA QUE DESEJA ALTERAR: "))

    except ValueError:
        print("\nDIGITE APENAS VALORES NUMERICOS. ")
        sleep(2)

    else:
        consult = f"""SELECT * FROM HORTA WHERE COD_HORTA = {id}"""

        inst_consult.execute(consult)
        data = inst_consult.fetchall()

        for oneData in data:
            datalist.append(oneData)

        if len(datalist) == 0:
            print(f"""\nID {id} NÃO CADASTRADO""")
            sleep(2)

        else:
            try:
                opt = int(input("""\n1 - ID
2 - NOME
3 - CAPACIDADE
0 - SAIR

SELECIONE QUAL DADO DESEJA ALTERAR: """))

            except ValueError:
                print("\nDIGITE APENAS VALORES NUMERICOS. ")
                sleep(2)

            else:
                # ALTERAR ID DA HORTA
                if opt == 1:
                    try:
                        newId = int(input("\nNOVO ID: "))

                        alter = f"""UPDATE HORTA SET COD_HORTA = {newId} WHERE COD_HORTA = {id}"""

                        inst_update.execute(alter)
                        conn.commit()

                    except ValueError:
                        print("\nDIGITE APENAS VALORES NUMERICOS.")
                        sleep(2)

                    except oracledb.IntegrityError as e:
                        error, = e.args
                        if error.code == 1438:
                            print("\nO CAMPO TEM NO MAXIMO 5 CARACTERES (XXXXX)")
                            sleep(2)

                        elif error.code == 1:
                            print("\nO CODIGO DA HORTA JÁ EXISTE")
                            sleep(2)

                        elif error.code == 1400:
                            print("\nPREENCHA TODOS OS DADOS")
                            sleep(2)

                        else:
                            print("\nERRO IntegrityError: ", error.code)
                            sleep(2)

                    except Exception as e:
                        print("\nERRO: ", e)
                        sleep(2)

                    else:
                        print("\nATUALIZAÇÃO REALIZADA.")
                        sleep(2)

                # ALTERAR NOME DA HORTA
                elif opt == 2:
                    try:
                        newName = input("\nNOVO NOME: ").upper()

                        alter = f"""UPDATE HORTA SET NOME_HORTA = '{newName}' WHERE COD_HORTA = {id}"""

                        inst_update.execute(alter)
                        conn.commit()

                    except oracledb.IntegrityError as e:
                        error, = e.args
                        if error.code > 0:
                            print("\nERRO IntegrityError: ", error.code)
                            sleep(2)

                    except oracledb.DatabaseError as e:
                        error, = e.args
                        if error.code == 12899:
                            print("\nLIMITE DE CARACTERES TEXTO ATINGIDO.")
                            sleep(2)

                        else:
                            print("\nERRO DatabaseError: ", error.code)

                    except Exception as e:
                        print("\nERRO: ", e)
                        sleep(2)

                    else:
                        print("\nATUALIZAÇÃO REALIZADA.")
                        sleep(2)

                # ALTERAR CAPACIDADE DA HORTA
                elif opt == 3:
                    try:
                        newStorage = int(input("\nNOVO E-MAIL: "))

                        alter = f"""UPDATE HORTA SET CAPACIDADE_PLANTIO = {newStorage} WHERE COD_HORTA = {id}"""

                        inst_update.execute(alter)
                        conn.commit()

                    except ValueError:
                        print("\nDIGITE APENAS VALORES NUMERICOS.")
                        sleep(2)

                    except oracledb.IntegrityError as e:
                        error, = e.args
                        if error.code > 0:
                            print("\nERRO IntegrityError: ", error.code)
                            sleep(2)

                    except oracledb.DatabaseError as e:
                        error, = e.args
                        if error.code == 12899:
                            print("\nLIMITE DE CARACTERES TEXTO ATINGIDO.")
                            sleep(2)

                        else:
                            print("\nERRO DatabaseError: ", error.code)

                    except Exception as e:
                        print("\nERRO: ", e)
                        sleep(2)

                    else:
                        print("\nATUALIZAÇÃO REALIZADA.")
                        sleep(2)

                elif opt == 0:
                    print("\nVOLTE SEMPRE!")
                    connection = False

                else:
                    print("\nDIGITE UMA OPÇÃO VÁLIDA")
                    sleep(2)


# FUNÇÃO P/ EXCLUIR OS DADOS DE UMA HORTA
def delete():
    try:
        dataList = []
        id = int(input("\nDIGITE O ID DA HORTA QUE DESEJA EXCLUIR: "))

        consult = f"""SELECT * FROM HORTA WHERE COD_HORTA = {id}"""

        inst_consult.execute(consult)
        data = inst_consult.fetchall()

        for oneData in data:
            dataList.append(oneData)

        if len(dataList) == 0:
            print("\nID NÃO CADASTRADO.")
            sleep(2)

        else:
            try:
                delete = f"""DELETE FROM HORTA WHERE COD_HORTA = {id}"""

                inst_delete.execute(delete)
                conn.commit()

            except:
                print("\nERRO BANCO DE DADOS.")
                sleep(2)

            else:
                print("\nDADOS EXCLUIDOS.")
                sleep(2)

    except Exception as e:
        print(e)
