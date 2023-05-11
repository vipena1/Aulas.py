"""Integração do programa Python com a mesma base de dados que o sistema web tem;

 O programa deve ter ao menos 2 menus (telas) com interação com BD;

 Cada menu deve ler (SELECT) informações do BD; ? Cada menu deve escrever (INSERT, UPDATE ou DELETE) no BD;

 Todas as informações alteradas através do programa python, devem ser refletidas no sistema web. """

import oracledb as orcl
import pandas as pd
from faker import Faker

fake = Faker('pt_BR')

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

        else:
            # USANDO A ENTIDADE DE USUÁRIO
            if opt == 1:
                try:
                    opt = int(input("""\nQUAL AÇÃO DESEJA EXECUTAR NO USUÁRIO?
1 - VISUALIZAR.
2 - REGISTRAR.
3 - ALTERAR.
4 - EXCLUIR.
QUAL OPÇÃO DESEJA SELECIONAR? """))

                except ValueError:
                    print("Digite apenas o número da opção desejada.")

                # VISUALIZAR OS ATRIBUTOS DOS USUÁRIOS
                if opt == 1:
                    try:
                        dataList = []

                        inst_consult.execute('SELECT * FROM USUARIOB3')

                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(oneData)

                        dataList = sorted(dataList)

                        dataDf = pd.DataFrame.from_records(dataList, columns=['NOME', 'CPF', 'EMAIL', 'NASCIMENTO', 'CEP',
                                                                              'ENDEREÇO', 'NÚMERO', 'COMPLEMENTO', 'BAIRRO', 'UF'], index='CPF')
                        if (dataDf.empty):
                            print("Não há registros")
                        else:
                            print(dataDf)
                        print("\n")

                    except Exception as e:
                        print(e)

                # CADASTRANDO ATRIBUTOS NOS USUÁRIOS
                elif opt == 2:
                    try:
                        nome = fake.name()  # input("Nome:  ")
                        cpf = fake.cpf()  # int(input("CPF: "))
                        email = fake.email()  # input("EMAIL: ")
                        nascimento = input("NASCIMENTO: ")
                        cep = fake.random_int(10000000, 99999999)  # input("CEP: ")
                        endereco = fake.text(30)  # input("ENDEREÇO: ")
                        numero = fake.random_int(1, 99999)  # int(input("NÚMERO: "))
                        complemento = fake.text(20)  # input("COMPLEMENTO: ")
                        bairro = fake.text(20)  # input("BAIRRO: ")
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

                # ALTERAR DADOS DO USUÁRIO
                elif opt == 3:
                    dataList = []

                    cpf = input("Digite o CPF do usuário que você deseja alterar: ")

                    consult = f"""SELECT * FROM USUARIOB3 WHERE CPF = '{cpf}'"""

                    inst_consult.execute(consult)
                    data = inst_consult.fetchall()

                    for oneData in data:
                        dataList.append(oneData)

                    if len(dataList) == 0:
                        print("O CPF não existe.")

                    else:
                        try:
                            opt = int(input("""\n
1 - NOME
2 - CPF
3 - EMAIL
4 - DATA DE NASCIMENTO
5 - CEP
6 - ENDERECO
7 - NUMERO
8 - COMPLEMENTO
9 - BAIRRO
10 - UF
Qual dado você deseja alterar? """))

                        except ValueError:
                            print("\nDigite valores numéricos! ")

                        # ALTERAR O NOME DO USUARIO
                        if opt == 1:
                            try:
                                newName = input("\nNovo nome: ")

                                alter = f"""update usuariob3 set NOME = '{newName}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR O CPF DO USUARIO
                        elif opt == 2:
                            try:
                                newCpf = input("\nNovo CPF: ")

                                alter = f"""update usuariob3 set CPF = '{newCpf}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR O EMAIL DO USUARIO
                        elif opt == 3:
                            try:
                                newEmail = input("\nNovo Email: ")

                                alter = f"""update usuariob3 set EMAIL = '{newEmail}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR O NASCIMENTO DO USUARIO
                        elif opt == 4:
                            try:
                                newNascimento = input("\nNova data de nascimento: ")

                                alter = f"""update usuariob3 set NASCIMENTO = '{newNascimento}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR O CEP DO USUARIO
                        elif opt == 5:
                            try:
                                newCep = input("\nNovo CEP: ")

                                alter = f"""update usuariob3 set CEP = '{newCep}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR O ENDEREÇO DO USUARIO
                        elif opt == 6:
                            try:
                                newEndereco = input("\nNovo endereço: ")

                                alter = f"""update usuariob3 set ENDERECO = '{newEndereco}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR O NUMERO DO USUARIO
                        elif opt == 7:
                            try:
                                newNumero = int(input("\nNovo número: "))

                                alter = f"""update usuariob3 set NUMERO = {newNumero} where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except ValueError:
                                print("\nDigite um valor numerico")

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR O COMPLEMENTO DO USUARIO
                        elif opt == 8:
                            try:
                                newComplemento = input("\nNovo complemento: ")

                                alter = f"""update usuariob3 set COMPLEMENTO = '{newComplemento}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR O BAIRRO DO USUARIO
                        elif opt == 9:
                            try:
                                newBairro = input("\nNovo bairro: ")

                                alter = f"""update usuariob3 set BAIRRO = '{newBairro}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR A UF DO USUARIO
                        elif opt == 10:
                            try:
                                newUf = input("\nNova UF: ")

                                alter = f"""update usuariob3 set UF = '{newUf}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        else:
                            print("\nDigite um  valor valido")

                # EXCLUIR DADOS DO USUÁRIO
                elif opt == 4:
                    try:
                        dataList = []

                        cpf = input("\nDigite o CPF do usuário que deseja excluir: ")

                        consult = f"""SELECT * FROM usuariob3 WHERE cpf = '{cpf}'"""

                        inst_consult.execute(consult)
                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(data)

                        if len(dataList) == 0:
                            print("O cpf digitado não existe")

                        else:
                            try:
                                delete = f"""delete from usuariob3 where cpf = '{cpf}'"""
                                inst_delete.execute(delete)
                                conn.commit()

                            except:
                                print("Erro banco de  dados")

                            else:
                                print("Dados excluidos")

                    except Exception as e:
                        print(e)

                # CASO DIGITE UM NÚMEMRO QUE NÃO EXISTA DE OPÇÃO
                else:
                    print("Digite uma opção valida")

            # USANDO A ENTIDADE DE EMPRESA
            elif opt == 2:
                try:
                    opt = int(input("""\nQUAL AÇÃO DESEJA EXECUTAR NA EMPRESA?
1 - VISUALIZAR.
2 - REGISTRAR.
3 - ALTERAR.
4 - EXCLUIR.
QUAL OPÇÃO DESEJA SELECIONAR? """))

                except ValueError:
                    print("\nDigite apenas o número da opção desejada.")

                # VISUALIZAR OS ATRIBUTOS DAS EMPRESAS
                if opt == 1:
                    try:
                        dataList = []

                        inst_consult.execute('SELECT * FROM EMPRESAB3')

                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(oneData)

                        dataList = sorted(dataList)

                        dataDf = pd.DataFrame.from_records(dataList, columns=['NOME', 'CNPJ', 'ANO DE ABERTURA'], index='CNPJ')
                        if (dataDf.empty):
                            print("Não há registros")
                        else:
                            print(dataDf)
                        print("\n")

                    except Exception as e:
                        print(e)

                # CADASTRANDO ATRIBUTOS NA EMPRESA
                elif opt == 2:
                    try:
                        nome = fake.name()  # input("Nome:  ")
                        cnpj = fake.cnpj()  # int(input("CNPJ: "))
                        abertura = fake.random_int(1000, 9999)  # input("DATA DE ABERTURA: ")


                        cadastro = f"""INSERT INTO EMPRESAB3 (NOME, CNPJ, ANOABERTURA) VALUES ('{nome}', '{cnpj}', {abertura}) """

                        inst_register.execute(cadastro)
                        conn.commit()
                    except ValueError:
                        print("Digite valores numéricos! ")

                    except:
                        print("Erro BD")

                    else:
                        print("Dados cadastrados!")

                # ALTERAR DADOS DO EMPRESA
                elif opt == 3:
                    dataList = []

                    cnpj = input("Digite o CNPJ do usuário que você deseja alterar: ")

                    consult = f"""SELECT * FROM EMPRESAB3 WHERE CNPJ = '{cnpj}'"""

                    inst_consult.execute(consult)
                    data = inst_consult.fetchall()

                    for oneData in data:
                            dataList.append(oneData)

                    if len(dataList) == 0:
                        print("O CNPJ não existe.")

                    else:
                        try:
                            opt = int(input("""\n
    1 - NOME
    2 - CNPJ
    3 - ANO DE ABERTURA
    Qual dado você deseja alterar? """))

                        except ValueError:
                            print("\nDigite valores numéricos! ")

                        # ALTERAR O NOME DA EMPRESA
                        if opt == 1:
                            try:
                                newName = input("\nNovo nome: ")

                                alter = f"""update EMPRESAB3 set NOME = '{newName}' where CNPJ = '{cnpj}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR O CNPJ DA EMPRESA
                        elif opt == 2:
                            try:
                                newCnpj = input("\nNovo CNPJ: ")

                                alter = f"""update EMPRESAB3 set CNPJ = '{newCnpj}' where CNPJ = '{cnpj}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR O ANO DE ABERTURA DA EMPRESA
                        elif opt == 3:
                            try:
                                newAbertura = int(input("\nNovo ano de abertura: "))

                                alter = f"""update usuariob3 set EMAIL = {newAbertura} where cpf = '{cnpj}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except ValueError:
                                print("\nDigite um valor numérico")

                            except:
                                print("Erro banco de dados")

                            else:
                                print("\nAtualização realizada!")

                # EXCLUIR DADOS DA EMPRESA
                elif opt == 4:
                    try:
                        dataList = []

                        cnpj = input("\nDigite o CNPJ do usuário que deseja excluir: ")

                        consult = f"""SELECT * FROM EMPRESAB3 WHERE CNPJ = '{cnpj}'"""

                        inst_consult.execute(consult)
                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(data)

                        if len(dataList) == 0:
                            print("O CNPJ digitado não existe")

                        else:
                            try:
                                delete = f"""delete from EMPRESAB3 where CNPJ = '{cnpj}'"""
                                inst_delete.execute(delete)
                                conn.commit()

                            except:
                                print("Erro banco de  dados")

                            else:
                                print("Dados excluidos")

                    except Exception as e:
                        print(e)

                # CASO DIGITE UM NÚMEMRO QUE NÃO EXISTA DE OPÇÃO
                else:
                    print("Digite uma opção valida")

            elif opt == 0:
                print("Volte sempre!")
                connection = False

            else:
                print("Digite uma opção valida")

    # SE O USUARIO NÃO FOR ADM
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

        else:
            # SIMULADOR
            if opt == 1:
                print("01")

            # DOCUMENTAÇÃO
            elif opt == 2:
                print("02")

            # INFORMAÇÕES
            elif opt == 3:
                print("03")

            # SAIR
            elif opt == 0:
                print("Volte sempre!")
                connection = False

            else:
                print("Digite uma opção valida")
