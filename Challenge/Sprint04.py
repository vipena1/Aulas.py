"""Integração do programa Python com a mesma base de dados que o sistema web tem;

 O programa deve ter ao menos 2 menus (telas) com interação com BD;

 Cada menu deve ler (SELECT) informações do BD; ? Cada menu deve escrever (INSERT, UPDATE ou DELETE) no BD;

 Todas as informações alteradas através do programa python, devem ser refletidas no sistema web. """

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

    # Usuario e senha para validação de usuário administrador
    user = input("DIGITE O USUÁRIO: ")
    password = input("DIGITE A SENHA: ")

while (connection == True):

    # Se o usuário digitado for o de administrador...
    if user == "ADM" and password == "ADMIN123":
        try:
            opt = int(input("""\nMenu de administrador.
1 - DADOS DOS USUÁRIOS.
2 - DADOS DAS EMPRESAS.
0 - SAIR
DIGITE A OPÇÃO DESEJADA: """))

        except ValueError:
            print("Digite apenas o número da opção desejada.")

        if opt == 1:
            # USANDO A ENTIDADE DE USUÁRIO
            try:
                opt = int(input("""\nQUAL AÇÃO DESEJA EXECUTAR NO USUÁRIO?
1 - VISUALIZAR.
2 - REGISTRAR.
3 - ALTERAR.
4 - EXCLUIR.
QUAL OPÇÃO DESEJA SELECIONAR? """))

            except ValueError:
                print("Digite apenas o número da opção desejada.")

            if opt == 1:
                # VISUALIZAR OS ATRIBUTOS DOS USUÁRIOS
                try:
                    dataList = []

                    inst_consult.execute('SELECT * FROM USUARIOB3')

                    data = inst_consult.fetchall()

                    for oneData in data:
                        dataList.append(oneData)

                    dataList = sorted(dataList)

                    dataDf = pd.DataFrame.from_records(dataList,
                                                         columns=['NOME', 'CPF', 'EMAIL', 'NASCIMENTO', 'CEP',
                                                                  'ENDEREÇO', 'NÚMERO', 'COMPLEMENTO', 'BAIRRO', 'UF'], index='CPF')
                    if (dataDf.empty):
                        print("Não há registros")
                    else:
                        print(dataDf)
                    print("\n")

                except Exception as e:
                    print(e)

            elif opt == 2:
                # INSERIR ATRIBUTOS NOS USUÁRIOS
                try:
                    nome = input("Nome: ")
                    cpf = int(input("CPF: "))
                    email = input("EMAIL: ")
                    nascimento = input("NASCIMENTO: ")
                    cep = input("CEP: ")
                    endereco = input("ENDEREÇO: ")
                    numero = int(input("NÚMERO: "))
                    complemento = input("COMPLEMENTO: ")
                    bairro = input("BAIRRO: ")
                    uf = input("UF: ")

                    cadastro = f"""INSERT INTO USUARIOB3 (NOME, CPF, EMAIL, NASCIMENTO, CEP, ENDERECO, NUMERO, COMPLEMENTO, BAIRRO, UF) VALUES ('{nome}', '{cpf}', '{email}', '{nascimento}', '{cep}', '{endereco}', {numero}, '{complemento}', '{bairro}', '{uf}') """

                    inst_register.execute(cadastro)
                    conn.commit()
                except ValueError:
                    print("Digite valores numéricos! ")

                except:
                    print("Erro BD")

                else:
                    print("Dados cadastrados!")




        elif opt == 0:
            connection = False







    # Se o usuário não for administrador
    else:

        try:
            opt = int(input("""\nBEM-VINDO!
PARA NAVEGAR ENTRE OS MENUS, DIGITE O NÚMERO DESEJADO:
1 - SIMULADOR
2 - DOCUMENTAÇÃO
3 - INFORMAÇÕES
0 - SAIR
QUAL OPÇÃO DESEJA SELECIONAR? """))

        except ValueError:
            print("Digite apenas o número da opção desejada.")


