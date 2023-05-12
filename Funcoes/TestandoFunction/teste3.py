# Função para opção 3 - Relatorio

import oracledb as orcl
import pandas as pd
from time import sleep

connection = False

try:
    # Abrindo conexão com o banco
    dnStr = orcl.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = orcl.connect(user = "RM96881", password = "250998", dsn = dnStr)

    inst_consult = conn.cursor()
    inst_register = conn.cursor()
    inst_update = conn.cursor()
    inst_delete = conn.cursor()
    inst_report = conn.cursor()

except Exception as e:
    # Se der erro retornara o motivo
    print("Erro: ", e)
    connection = False

else:
    connection = True

def relatorio():
    dataList = []

    cargo_id = int(input("Digite o ID do cargo que deseja visualizar os funcionarios: "))

    report = f"""select FUNCIONARIO_ID, FUNCIONARIO_CPF, FUNCIONARIO_NOME, FUNCIONARIO_SALARIO, FUNCIONARIO_IDADE 
    from FUNCIONARIOS inner join CARGOS on funcionarios.CARGO_ID = cargos.CARGO_ID WHERE cargos.CARGO_ID = {cargo_id} order by 1"""

    inst_report.execute(report)
    data = inst_report.fetchall()

    for oneData in data:
        dataList.append(oneData)

    dataList = sorted(dataList)

    dataDf = pd.DataFrame.from_records(dataList, columns=['ID', 'CPF', 'NOME', 'SALARIO', 'IDADE'], index='ID')

    if (dataDf.empty):
        print("\nNão há registros")
        sleep(2)
    else:
        print(dataDf)
        sleep(2)
    print("\n")
