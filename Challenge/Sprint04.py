"""Integração do programa Python com a mesma base de dados que o sistema web tem;

 O programa deve ter ao menos 2 menus (telas) com interação com BD;

 Cada menu deve ler (SELECT) informações do BD; ? Cada menu deve escrever (INSERT, UPDATE ou DELETE) no BD;

 Todas as informações alteradas através do programa python, devem ser refletidas no sistema web. """

import oracledb as orcl

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
    conexao = False

else:
    conexao = True

while (conexao == True):
    # Usuario e senha para validação de usuário administrador
    user = input("DIGITE O USUÁRIO: ")
    password = input("DIGITE A SENHA: ")

    # Se o usuário digitado for o de administrador...
    if user == "ADM" and password == "ADMIN123":
        try:
            opt = int(input("""\nMenu de administrador.
1 - ALTERAR DADOS DE USUÁRIO.
2 - ALTERAR DADOS DE EMPRESAS.
0 - SAIR
DIGITE A OPÇÃO DESEJADA: """))

        except ValueError:
            print("Digite apenas o número da opção desejada.")

    else:

        try:
            # Menu de usuário comum sem ser administrador
            opc = int(input("""\nBEM-VINDO!
PARA NAVEGAR ENTRE OS MENUS, DIGITE O NÚMERO DESEJADO:
1 - SIMULADOR
2 - DOCUMENTAÇÃO
3 - INFORMAÇÕES
0 - SAIR
QUAL OPÇÃO DESEJA SELECIONAR? """))

        except ValueError:
            print("Digite apenas o número da opção desejada.")


