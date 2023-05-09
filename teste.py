import oracledb as orcl
import pandas as pd

try:
    # Abrindo conexão com o banco
    dnStr = orcl.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = orcl.connect(user = "RM96881", password = "250998", dsn = dnStr)

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

dataList = []
inst_consult.execute("SELECT * FROM USUARIOB3")

data = inst_consult.fetchall()

for dado in data:
    dataList.append(dado)

dataList = sorted(dataList)

dataDf = pd.DataFrame.from_records(dataList, columns = ["NOME", "CPF", "EMAIL", "NASCIMENTO", "CEP", "ENDERECO", "NUMERO", "COMPLEMENTO", "BAIRRO", "UF"], index= "CPF")

if (dataDf.empty):
    print("Não há registros")

else:
    print(dataDf)
print("\n")
