import teste1
import teste2
import teste3
import oracledb as orcl
from time import sleep

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

while connection == True:

    try:
        opt = int(input("""\nSelecione a opção desejada.
1 - DADOS DOS FUNCIONARIOS.
2 - DADOS DOS CARGOS.
3 - RELATORIO
0 - SAIR
DIGITE A OPÇÃO DESEJADA: """))

    except ValueError:
        print("\nDigite apenas o número da opção desejada.")
        sleep(2)

    else:

        # USANDO A ENTIDADE DE FUNCIONARIOS
        if opt == 1:
            teste1.funcionario()

        # USANDO A ENTIDADE DE CARGOS
        elif opt == 2:
            teste2.cargo()

        # RELATORIO
        elif opt == 3:
            teste3.relatorio()

        elif opt == 0:
            print("Volte sempre")
            connection = False