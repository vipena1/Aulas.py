# Funções para entidade plantacao

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
    inst_consumption = conn.cursor()

except Exception as e:
    # Se der erro retornara o motivo
    print("Erro: ", e)
    connection = False

else:
    connection = True


# FUNÇÃO P/ INSERIR NOVO LANÇAMENTO NA PLANTACAO
def insert():
    try:
        # COLETA DE DADOS DA PLANTACAO
        idPlantation = int(input("\nCODIGO DA PLATAÇÃO: "))
        idUser = int(input("CODIGO DO USUÁRIO: "))
        idFood = int(input("CODIGO DO ALIMENTO: "))
        idGarden = int(input("CODIGO DA HORTA: "))
        row = int(input("FILEIRA PLANTADA: "))
        position = int(input("POSIÇÃO DA FILEIRA: "))
        qtyPlantation = int(input("QNTD PLATADA: "))

        # CONSULTA PARA VER A QUANTIDADE NO ESTOQUE.
        consultQty = f"""SELECT QNTD_SEMENTE_ALIMENTO FROM ALIMENTO WHERE COD_ALIMENTO = {idFood} """

        inst_consult.execute(consultQty)
        currentQty = inst_consult.fetchall()

        if (currentQty[0][0] - qtyPlantation) < 0:
            print("\nPLANTAÇÃO NÃO REALIZADA")

        else:

            # COMANDO P/ REGISTRO NO SQL
            register = f"""INSERT INTO PLANTACAO VALUES ({idPlantation}, {idUser}, {idFood}, {idGarden}, {row}, {position}, {qtyPlantation})"""

            # EXECUÇÃO DO COMANDO
            inst_register.execute(register)
            # COMMIT P/ SALVAR OS DADOS INSERIDOS
            conn.commit()

            # COMANDO P/ CONSUMIR A QUANTIDADE DE SEMENTES DO ALIMENTO
            consumption = f"""UPDATE ALIMENTO SET QNTD_SEMENTE_ALIMENTO = (QNTD_SEMENTE_ALIMENTO - {qtyPlantation}) where COD_ALIMENTO = {idFood}"""

            inst_consumption.execute(consumption)
            conn.commit()

    except ValueError:
        print("\nPREENCHA TODOS OS CAMPOS COM NÚMEROS.")
        sleep(2)

    except IndexError:
        print("\nALIMENTO NÃO ENCONTRADO.")
        sleep(2)

    except oracledb.IntegrityError as e:
        error, = e.args
        if error.code == 1438:
            print("\nOS CAMPOS TEM NO MAXIMO 5 CARACTERES (XXXXX)")
            sleep(2)

        elif error.code == 1:
            print("\nO CODIGO DA PLANTAÇÃO JÁ EXISTE")
            sleep(2)

        else:
            print("\nERRO IntegrityError: ", error.code)
            sleep(2)

    except Exception as e:
        print("\nERRO: ", e)
        sleep(2)

    else:
        if (currentQty[0][0] - qtyPlantation) < 0:
            print("A QUANTIDADE DE SEMENTES NO ESTOQUE NÃO PODE SER NEGATIVA.")
            sleep(2)

        else:
            print("\nPLANTAÇÃO REALIZADA.")
            sleep(2)


# FUNÇÃO P/ LER A TABELA PLANTACAO
def consult():
    try:
        # LISTA DE DADOS VAZIA P/ SER ADICIONADO OS DADOS DE LEITURA
        dataList = []

        # COMANDO P/ CONSULTA NO SQL
        inst_consult.execute("""SELECT COD_PLANTACAO, NOME, NOME_HORTA, NOME_ALIMENTO, FILEIRA, POSICAO, QNTD_PLANTADA FROM PLANTACAO
inner join USUARIO on PLANTACAO.COD_USUARIO = USUARIO.COD_USUARIO 
inner join ALIMENTO on  PLANTACAO.COD_ALIMENTO = ALIMENTO.COD_ALIMENTO
inner join HORTA on PLANTACAO.COD_HORTA = HORTA.COD_HORTA order by 1""")

        # COMANDO P/BUSCAR OS DADOS
        data = inst_consult.fetchall()

        # LOOP P/ SALVAR OS DADOS DENTRO DA LISTA
        for oneData in data:
            dataList.append(oneData)

        dataList = sorted(dataList)

        dataDf = pd.DataFrame.from_records(dataList,
                                           columns=['ID', 'NOME_USUARIO', 'HORTA', 'ALIMENTO', 'FILEIRA', 'POSICAO',
                                                    'QNTD_PLANTADA'],
                                           index='ID')

        if dataDf.empty:
            print("\nNÃO HÁ REGISTRO DE PLANTAÇÕES")
            sleep(2)

        else:
            print(dataDf)
            sleep(2)

    except Exception as e:
        print('\n', e)
        sleep(2)


# FUNÇÃO P/ ALTERAR OS DADOS DE UMA PLANTACAO
def alter():
    try:
        datalist = []

        id = int(input("\nDIGITE O ID DA PLATAÇÃO QUE DESEJA ALTERAR: "))

    except ValueError:
        print("\nDIGITE APENAS VALORES NUMERICOS. ")
        sleep(2)

    else:
        consult = f"""SELECT * FROM PLANTACAO WHERE COD_PLANTACAO = {id}"""

        inst_consult.execute(consult)
        data = inst_consult.fetchall()

        for oneData in data:
            datalist.append(oneData)

        if len(datalist) == 0:
            print(f"""\nID {id} NÃO CADASTRADO""")
            sleep(2)

        else:
            try:
                opt = int(input("""\n1 - ID PLANTAÇÃO
2 - ID USUÁRIO
3 - ID ALIMENTO
4 - ID HORTA
5 - FILEIRA PLANTADA
6 - POSIÇÃO PLANTADA
7 - QUANTIDADE PLANTADA
0 - SAIR

SELECIONE QUAL DADO DESEJA ALTERAR: """))

            except ValueError:
                print("\nDIGITE APENAS VALORES NUMERICOS. ")
                sleep(2)

            else:
                # ALTERAR ID DA PLANTACAO
                if opt == 1:
                    try:
                        newIdPlantation = int(input("\nNOVO ID PLANTAÇÃO: "))

                        alter = f"""UPDATE PLANTACAO SET COD_PLANTACAO = {newIdPlantation} WHERE COD_PLANTACAO = {id}"""

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
                            print("\nO CODIGO DA PLANTAÇÃO JÁ EXISTE")
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

                # ALTERAR ID DA USUARIO
                elif opt == 2:
                    try:
                        newIdUser = int(input("\nNOVO ID USUARIO: "))

                        alter = f"""UPDATE PLANTACAO SET COD_USUARIO = {newIdUser} WHERE COD_PLANTACAO = {id}"""

                        inst_update.execute(alter)
                        conn.commit()


                    except oracledb.IntegrityError as e:
                        error, = e.args
                        if error.code == 1438:
                            print("\nO CAMPO TEM NO MAXIMO 5 CARACTERES (XXXXX)")
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

                # ALTERAR ID DA ALIMENTO
                elif opt == 3:
                    try:
                        newIdFood = int(input("\nNOVO ID DO ALIMENTO: "))

                        alter = f"""UPDATE PLANTACAO SET COD_ALIMENTO = {newIdFood} WHERE COD_PLANTACAO = {id}"""

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

                        else:
                            print("\nERRO IntegrityError: ", error.code)
                            sleep(2)

                    except Exception as e:
                        print("\nERRO: ", e)
                        sleep(2)

                    else:
                        print("\nATUALIZAÇÃO REALIZADA.")
                        sleep(2)

                # ALTERAR ID DA HORTA
                elif opt == 4:
                    try:
                        newIdGarden = int(input("\nNOVO ID DO HORTA: "))

                        alter = f"""UPDATE PLANTACAO SET COD_HORTA = {newIdGarden} WHERE COD_PLANTACAO = {id}"""

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

                        else:
                            print("\nERRO IntegrityError: ", error.code)
                            sleep(2)

                    except Exception as e:
                        print("\nERRO: ", e)
                        sleep(2)

                    else:
                        print("\nATUALIZAÇÃO REALIZADA.")
                        sleep(2)

                # ALTERAR FILEIRA
                elif opt == 5:
                    try:
                        newRow = int(input("\nNOVA FILEIRA: "))

                        alter = f"""UPDATE PLANTACAO SET FILEIRA = {newRow} WHERE COD_PLANTACAO = {id}"""

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

                        else:
                            print("\nERRO IntegrityError: ", error.code)
                            sleep(2)

                    except Exception as e:
                        print("\nERRO: ", e)
                        sleep(2)

                    else:
                        print("\nATUALIZAÇÃO REALIZADA.")
                        sleep(2)

                # ALTERAR POSIÇÃO
                elif opt == 6:
                    try:
                        newPositino = int(input("\nNOVA POSIÇÃO: "))

                        alter = f"""UPDATE PLANTACAO SET POSICAO = {newPositino} WHERE COD_PLANTACAO = {id}"""

                        inst_update.execute(alter)
                        conn.commit()

                    except ValueError:
                        print("\nDIGITE APENAS VALORES NUMERICOS.")
                        sleep(2)

                    except oracledb.IntegrityError as e:
                        error, = e.args
                        if error.code == 1438:
                            print("\nOS CAMPOS TEM NO MAXIMO 5 CARACTERES (XXXXX)")
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

                # ALTERAR QUANTIDADE PLANTADA
                elif opt == 7:
                    try:
                        newQtyPlantation = int(input("\nNOVA QUANTIDADE PLANTADA: "))

                        alter = f"""UPDATE PLANTACAO SET QNTD_PLANTADA = {newQtyPlantation} WHERE COD_PLANTACAO = {id}"""

                        inst_update.execute(alter)
                        conn.commit()

                    except ValueError:
                        print("\nDIGITE APENAS VALORES NUMERICOS.")
                        sleep(2)

                    except oracledb.IntegrityError as e:
                        error, = e.args
                        if error.code == 1438:
                            print("\nOS CAMPOS TEM NO MAXIMO 5 CARACTERES (XXXXX)")
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

                elif opt == 0:
                    print("\nVOLTE SEMPRE!")
                    connection = False

                else:
                    print("\nDIGITE UMA OPÇÃO VÁLIDA")
                    sleep(2)


# FUNÇÃO P/ EXCLUIR OS DADOS DE UMA PLANTACAO
def delete():
    try:
        dataList = []
        id = int(input("\nDIGITE O ID DA PLANTAÇÃO QUE DESEJA EXCLUIR: "))

        consult = f"""SELECT * FROM PLANTACAO WHERE COD_PLANTACAO = {id}"""

        inst_consult.execute(consult)
        data = inst_consult.fetchall()

        for oneData in data:
            dataList.append(oneData)

        if len(dataList) == 0:
            print("\nID NÃO CADASTRADO.")
            sleep(2)

        else:
            try:
                delete = f"""DELETE FROM PLANTACAO WHERE COD_PLANTACAO = {id}"""

                inst_delete.execute(delete)
                conn.commit()

            except:
                print("\nERRO BANCO DE DADOS.")
                sleep(2)

            # verificar codigo de erro p/ quando não excluir por causa das relações existentes

            else:
                print("\nDADOS EXCLUIDOS.")
                sleep(2)

    except Exception as e:
        print(e)
