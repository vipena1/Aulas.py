# Funções para extração de relatórios

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
    inst_extract = conn.cursor()  # extrair relatorios

except Exception as e:
    # Se der erro retornara o motivo
    print("Erro: ", e)
    connection = False

else:
    connection = True


# FUNÇÃO PARA EXTRÁIR RELATÓRIO POR USUÁRIO
def reportUser():
    try:
        dataList = []

        id = int(input("\nDIGIE O CODIGO DO USUÁRIO QUE DESEJA EXTRAIR O RELATÓRIO: "))

        extract = f"""SELECT NOME, NOME_HORTA, NOME_ALIMENTO, FILEIRA, POSICAO FROM PLANTACAO
            INNER JOIN USUARIO ON PLANTACAO.COD_USUARIO = USUARIO.COD_USUARIO
            INNER JOIN HORTA ON PLANTACAO.COD_HORTA = HORTA.COD_HORTA
            INNER JOIN ALIMENTO ON PLANTACAO.COD_ALIMENTO = ALIMENTO.COD_ALIMENTO
            WHERE COD_USUARIO = {id}"""
        inst_extract.execute(extract)
        data = inst_consult.fetchall()

        for oneData in data:
            dataList.append(oneData)

        dataList = sorted(dataList)

        dataDf = pd.DataFrame.from_records(dataList, columns=['USUARIO', 'HORTA', 'ALIMENTO', 'FILEIRA', 'POSIÇÃO'],
                                           index='NOME')

        if dataDf.empty:
            print("\nUSUÁRIO NÃO NÃO EXISTE.")

        else:
            print(dataDf)
            sleep(2)

    except ValueError:
        print("\nDIGITE APENAS VALORES NUMÉRICOS.")

    except Exception as e:
        print('\n', e)
        sleep(2)


# FUNÇÃO PARA EXTRÁIR RELATÓRIO POR ALIMENTO
def reportFood():
    try:
        dataList = []

        id = int(input("\nDIGIE O CODIGO DO ALIMENTO QUE DESEJA EXTRAIR O RELATÓRIO: "))

        extract = f"""SELECT NOME_ALIMENTO, QNTD_PLANTADA, NOME_HORTA, FILEIRA, POSICAO FROM PLANTACAO
            INNER JOIN HORTA ON PLANTACAO.COD_HORTA = HORTA.COD_HORTA
            INNER JOIN ALIMENTO ON PLANTACAO.COD_ALIMENTO = ALIMENTO.COD_ALIMENTO
            WHERE COD_ALIMENTO = {id}"""

        inst_extract.execute(extract)
        data = inst_consult.fetchall()

        for oneData in data:
            dataList.append(oneData)

        dataList = sorted(dataList)

        dataDf = pd.DataFrame.from_records(dataList,
                                           columns=['ALIMENTO', 'QNTD PLANTADA', 'HORTA', 'FILEIRA', 'POSIÇÃO'],
                                           index='ALIMENTO')

        if dataDf.empty:
            print("\nALIMENTO NÃO EXISTE.")  # VERIFICAR OUTRA TRATATIVA DE ERRO

        else:
            print(dataDf)
            sleep(2)

    except ValueError:
        print("\nDIGITE APENAS VALORES NUMÉRICOS.")

    except Exception as e:
        print('\n', e)
        sleep(2)


# FUNÇÃO PARA EXTRÁIR RELATÓRIO POR HORTA
def reportGarden():
    try:
        dataList = []

        id = int(input("\nDIGIE O CODIGO DA HORTA QUE DESEJA EXTRAIR O RELATÓRIO: "))

        extract = f"""SELECT NOME_HORTA, FILEIRA, POSICAO, NOME_ALIMENTO FROM PLANTACAO
            INNER JOIN HORTA ON PLANTACAO.COD_HORTA = HORTA.COD_HORTA
            INNER JOIN ALIMENTO ON PLANTACAO.COD_ALIMENTO = ALIMENTO.COD_ALIMENTO
            WHERE COD_HORTA = {id}"""

        inst_extract.execute(extract)
        data = inst_consult.fetchall()

        for oneData in data:
            dataList.append(oneData)

        dataList = sorted(dataList)

        dataDf = pd.DataFrame.from_records(dataList,
                                           columns=['HORTA', 'FILEIRA', 'POSIÇÃO', 'ALIMENTO'],
                                           index='HORTA')

        if dataDf.empty:
            print("\nHORTA NÃO EXISTE.")  # VERIFICAR OUTRA TRATATIVA DE ERRO

        else:
            print(dataDf)
            sleep(2)

    except ValueError:
        print("\nDIGITE APENAS VALORES NUMÉRICOS.")

    except Exception as e:
        print('\n', e)
        sleep(2)
