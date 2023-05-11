import oracledb
import pandas as pd

try:
    dnStr = oracledb.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = oracledb.connect(user="RM96881",password="250998", dsn = dnStr)

    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()

except Exception as e:
    print("Erro: ", e)
    conexao = False
else:
    conexao = True

while (conexao==True):
    print("1-Inserção")
    print("2-Consulta")
    print("3-Relatório de todos os clientes com idade superior a 35 anos que residam na cidade de São Paulo")
    print("4-Relatório de todos os clientes que residam no Rio de Janeiro com limite de crédito superior a R$5000,00")
    print("5-Alterar")
    print("6-Excluir")
    print("7-Sair")

    opc = int(input("Digite a opção (1-5): "))

    if (opc==1):
        try:
            id = input("ID:")
            nome = input("Nome: ")
            logr = input("Logradouro: ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            idade = int(input("Idade: "))
            limite = float(input("Limite de Crédito: "))

            cadastro = f"""INSERT INTO clientes (ID,cliente_nome,cliente_logradouro,cliente_bairro,cliente_cidade,cliente_idade,cliente_limitecredito) VALUES ('{id}','{nome}','{logr}','{bairro}','{cidade}',{idade},{limite})"""

            inst_cadastro.execute(cadastro)
            conn.commit()
        except ValueError:
            print("Digite valores numéricos!")
        except:
            print("Erro de transação do BD")
        else:
            print("Dados cadastrados com sucesso!")
    elif (opc==2):
        lista_dados = []

        inst_consulta.execute('SELECT * FROM clientes')

        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

        lista_dados = sorted(lista_dados)

        dados_df = pd.DataFrame.from_records(lista_dados,columns = ['Id','Nome','Logradouro','Bairro','Cidade','Idade','Limite Credito'],index='Id')

        if (dados_df.empty):
            print("Não há registros")
        else:
            print(dados_df)
        print("\n")
    elif (opc==3):
        lista_dados = []
        relat1 = f"""SELECT * FROM clientes WHERE cliente_idade > 35 and cliente_cidade = 'Sao Paulo'"""

        inst_consulta.execute(relat1)

        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

            lista_dados = sorted(lista_dados)

            dados_df = pd.DataFrame.from_records(lista_dados,columns=['Id', 'Nome', 'Logradouro', 'Bairro', 'Cidade', 'Idade','Limite Credito'], index='Id')

            if (dados_df.empty):
                print("Não há registros")
            else:
                print(dados_df)
            print("\n")
    elif (opc==4):
        lista_dados = []
        relat2 = f"""SELECT * FROM clientes WHERE cliente_limitecredito > 5000 and cliente_cidade = 'Rio de Janeiro'"""

        inst_consulta.execute(relat2)

        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

            lista_dados = sorted(lista_dados)

            dados_df = pd.DataFrame.from_records(lista_dados,columns=['Id', 'Nome', 'Logradouro', 'Bairro', 'Cidade', 'Idade','Limite Credito'], index='Id')

            if (dados_df.empty):
                print("Não há registros")
            else:
                print(dados_df)
            print("\n")

    elif (opc==5):
        lista_dados = []

        id = int(input("Digite o ID que deseja alterar: "))

        consulta = f"""SELECT * FROM clientes WHERE id = {id} """

        inst_consulta.execute(consulta)
        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dado)

        if (len(lista_dados) == 0):
            print("O id digitado não existe.")

        else:
            try:
                novo_id = int(input("Novo ID:"))
                novo_nome = input("Novo Nome: ")
                novo_logr = input("Novo Logradouro: ")
                novo_bairro = input("Novo Bairro: ")
                novo_cidade = input("Novo Cidade: ")
                novo_idade = int(input("Novo Idade: "))
                novo_limite = float(input("Novo Limite de Crédito: "))

                alteracao = f"""UPDATE clientes SET ID = {novo_id}, cliente_nome = {novo_nome}, cliente_logradouro = {novo_logr},
                 cliente_bairro = {novo_bairro}, cliente_cidade = {novo_cidade},cliente_idade = {novo_idade},
                  cliente_limitecredito = {novo_limite} WHERE ID = {id}"""

                inst_alteracao.execute(alteracao)
                conn.commit()
            except ValueError:
                print("Digite valores numericos")
            except:
                print("Erro de transaÃ§Ã£o no BD")
            else:
                print("Dados atualizados com sucesso")

    elif (opc==6):
        lista_dados = []

        id = input("Digite o ID que deseja excluir: ")

        consulta = f"""SELECT * FROM clientes WHERE ID = {id}"""

        inst_consulta.execute(consulta)
        dados = inst_consulta.fetchall()

        for dado in dados:
            lista_dados.append(dados)

        if (len(lista_dados) ==0 ):
            print("O id digitado não existe")

        else:
            try:
                exclusao = f"""DELETE FROM clientes WHERE id = {id}"""

                inst_exclusao.execute(exclusao)
                conn.commit()

            except:
                print("Erro de transação no BD")

            else:print("Dados excluidos")

    elif (opc==7):
        conexao = False
