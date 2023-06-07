# Funções para entidade usuário

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


# FUNÇÃO P/ INSERIR NOVO USUÁRIO
def insert():
    try:
        # COLETA DE DADOS DO USUÁRIO
        id = int(input("\nCODIGO USUÁRIO: "))
        name = input("NOME: ").upper()
        email = input("E-MAIL: ").upper()
        cep = input("CEP (00000-000): ")
        street = input("RUA: ").upper()
        neighborhood = input("BAIRRO: ").upper()
        city = input("CIDADE: ").upper()
        uf = input("UF: ").upper()
        password = input("SENHA: ")

        # COMANDO P/ REGISTRO NO SQL
        register = f"""INSERT INTO USUARIO VALUES ({id}, '{name}', '{email}', '{cep}', '{street}', '{neighborhood}', 
                '{city}', '{uf}', '{password}')"""

        # EXECUÇÃO DO COMANDO
        inst_register.execute(register)
        # COMMIT P/ SALVAAR OS DADOS INSERIDOS
        conn.commit()

    except ValueError:
        print("\nDIGITE UM VALOR NUMERICO.")
        sleep(2)

    except oracledb.IntegrityError as e:
        error, = e.args
        if error.code == 1438:
            print("\nCOD POSSUI NO MAXIMO 5 CARACTERES.")
            sleep(2)

        elif error.code == 1:
            print("\nO CODIGO DO USUÁRIO JÁ EXISTE")
            sleep(2)

        elif error.code == 1400:
            print("\nPREENCHA TODOS OS DADOS")
            sleep(2)

        else:
            print("\nERRO IntegrityError: ", error.code)
            sleep(2)

    except oracledb.DatabaseError as e:
        error, = e.args
        if error.code == 12899:
            print("\nLIMITE DE CARACTERES TEXTO ATINGIDO.")
            sleep(2)

        else:
            print("\nERRO IntegrityError: ", error.code)
            sleep(2)

    except Exception as e:
        print("\nERRO", e)

    else:
        print("\nDADOS CADASTRADO")
        sleep(2)


# FUNÇÃO P/ LER A TABELA USUÁRIO
def consult():
    try:

        # LISTA DE DADOS VAZIA P/ SER ADICIONADO OS DADOS DE LEITURA
        dataList = []

        # COMANDO P/ CONSULTA NO SQL
        inst_consult.execute("SELECT * FROM USUARIO")

        # COMANDO P/BUSCAR OS DADOS
        data = inst_consult.fetchall()

        # LOOP P/ SALVAR OS DADOS DENTRO DA LISTA
        for oneData in data:
            dataList.append(oneData)

        dataList = sorted(dataList)

        dataDf = pd.DataFrame.from_records(dataList,
                                           columns=['ID', 'NOME', 'E-MAIL', 'CEP', 'RUA', 'BAIRRO', 'CIDADE', 'UF',
                                                    'SENHA'],
                                           index='ID')

        if dataDf.empty:
            print("\nNÃO HÁ REGISTRO NA TABELA DE USUÁRIOS")
            sleep(2)

        else:
            print(dataDf)
            sleep(2)

    except Exception as e:
        print('\n', e)
        sleep(2)


# FUNÇÃO P/ ALTERAR OS DADOS DE UM USUÁRIO
def alter():
    try:
        datalist = []

        id = int(input("\nDIGITE O ID DO USUÁRIO QUE DESEJA ALTERAR: "))

    except ValueError:
        print("\nDIGITE APENAS VALORES NUMERICOS. ")
        sleep(2)

    else:
        consult = f"""SELECT * FROM USUARIO WHERE COD_USUARIO = {id}"""

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
3 - E-MAIL
4 - CEP
5 - RUA
6 - BAIRRO
7 - CIDADE
8 - UF
9 - SENHA
0 - SAIR

SELECIONE QUAL DADO DESEJA ALTERAR: """))

            except ValueError:
                print("\nDIGITE APENAS VALORES NUMERICOS. ")
                sleep(2)

            else:
                # ALTERAR ID DO USUÁRIO
                if opt == 1:
                    try:
                        newId = int(input("\nNOVO ID: "))

                        alter = f"""UPDATE USUARIO SET COD_USUARIO = {newId} WHERE COD_USUARIO = {id}"""

                        inst_update.execute(alter)
                        conn.commit()

                    except ValueError:
                        print("\nDIGITE APENAS VALORES NUMERICOS.")
                        sleep(2)

                    except oracledb.IntegrityError as e:
                        error, = e.args
                        if error.code == 1438:
                            print("\nO CAMPO TEM NO MAXIM0 5 CARACTERES.")
                            sleep(2)

                        elif error.code == 1:
                            print("\nO CODIGO DO USUÁRIO JÁ EXISTE")
                            sleep(2)

                        elif error.code == 1400:
                            print("\nPREENCHA TODOS OS DADOS")
                            sleep(2)

                        else:
                            print("\nERRO IntegrityError: ", error.code)
                            sleep(2)

                    else:
                        print("\nATUALIZAÇÃO REALIZADA.")
                        sleep(2)

                # ALTERAR NOME DO USUÁRIO
                elif opt == 2:
                    try:
                        newName = input("\nNOVO NOME: ").upper()

                        alter = f"""UPDATE USUARIO SET NOME = '{newName}' WHERE COD_USUARIO = {id}"""

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

                # ALTERAR E-MAIL DO USUÁRIO
                elif opt == 3:
                    try:
                        newEmail = input("\nNOVO E-MAIL: ").upper()

                        alter = f"""UPDATE USUARIO SET EMAIL = '{newEmail}' WHERE COD_USUARIO = {id}"""

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

                # ALTERAR CEP DO USUÁRIO
                elif opt == 4:
                    try:
                        newCep = input("\nNOVO CEP (00000-000): ")

                        alter = f"""UPDATE USUARIO SET CEP = '{newCep}' WHERE COD_USUARIO = {id}"""

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

                # ALTERAR RUA DO USUÁRIO
                elif opt == 5:
                    try:
                        newStreet = input("\nNOVA RUA: ").upper()

                        alter = f"""UPDATE USUARIO SET RUA = '{newStreet}' WHERE COD_USUARIO = {id}"""

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

                # ALTERAR RUA DO USUÁRIO
                elif opt == 6:
                    try:
                        newNeighborhood = input("\nNOVO BAIRRO: ").upper()

                        alter = f"""UPDATE USUARIO SET BAIRRO = '{newNeighborhood}' WHERE COD_USUARIO = {id}"""

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

                # ALTERAR CIDADE DO USUÁRIO
                elif opt == 7:
                    try:
                        newCity = input("\nNOVA CIDADE: ").upper()

                        alter = f"""UPDATE USUARIO SET CIDADE = '{newCity}' WHERE COD_USUARIO = {id}"""

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

                # ALTERAR UF DO USUÁRIO
                elif opt == 8:
                    try:
                        newUf = input("\nNOVA UF: ").upper()

                        alter = f"""UPDATE USUARIO SET UF = '{newUf}' WHERE COD_USUARIO = {id}"""

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

                # ALTERAR SENHA DO USUÁRIO
                elif opt == 9:
                    try:
                        newPassword = input("\nNOVA SENHA: ")

                        alter = f"""UPDATE USUARIO SET SENHA = '{newPassword}' WHERE COD_USUARIO = {id}"""

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

                elif opt == 0:
                    print("\nVOLTE SEMPRE!")
                    connection = False

                else:
                    print("\nDIGITE UMA OPÇÃO VÁLIDA")
                    sleep(2)


# FUNÇÃO P/ EXCLUIR OS DADOS DE UM USUÁRIO
def delete():
    try:
        dataList = []
        id = int(input("\nDIGITE O ID DO USUÁRIO QUE DESEJA EXCLUIR: "))

        consult = f"""SELECT * FROM USUARIO WHERE COD_USUARIO = {id}"""

        inst_consult.execute(consult)
        data = inst_consult.fetchall()

        for oneData in data:
            dataList.append(oneData)

        if len(dataList) == 0:
            print("\nID NÃO CADASTRADO.")
            sleep(2)

        else:
            try:
                delete = f"""DELETE FROM USUARIO WHERE COD_USUARIO = {id}"""

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
