"""Integração do programa Python com a mesma base de dados que o sistema web tem;

 O programa deve ter ao menos 2 menus (telas) com interação com BD;

 Cada menu deve ler (SELECT) informações do BD; ? Cada menu deve escrever (INSERT, UPDATE ou DELETE) no BD;

 Todas as informações alteradas através do programa python, devem ser refletidas no sistema web. """

import oracledb as orcl
import pandas as pd
from faker import Faker
from time import sleep

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
            sleep(2)

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
                    print("\nDigite apenas o número da opção desejada.")
                    sleep(2)

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
                            sleep(2)
                        else:
                            print(dataDf)
                            sleep(2)
                        print("\n")

                    except Exception as e:
                        print(e)
                        sleep(2)

                # CADASTRANDO ATRIBUTOS NOS USUÁRIOS
                elif opt == 2:
                    try:
                        nome = input("Nome:  ").upper()  #fake.name()
                        cpf = input("CPF: ").upper()  #fake.cpf()
                        email = input("EMAIL: ").upper()  #fake.email()
                        nascimento = input("NASCIMENTO: ").upper()
                        cep = input("CEP: ").upper()  #fake.random_int(10000000, 99999999)
                        endereco = input("ENDEREÇO: ").upper()  #fake.text(30)
                        numero = int(input("NÚMERO: "))  #fake.random_int(1, 99999)
                        complemento = input("COMPLEMENTO: ").upper()  #fake.text(20)
                        bairro = input("BAIRRO: ").upper()  #fake.text(20)
                        uf = input("UF: ").upper()

                        cadastro = f"""INSERT INTO USUARIOB3 (NOME, CPF, EMAIL, NASCIMENTO, CEP, ENDERECO, NUMERO, COMPLEMENTO, BAIRRO, UF) VALUES ('{nome}', '{cpf}', '{email}', '{nascimento}', '{cep}', '{endereco}', {numero}, '{complemento}', '{bairro}', '{uf}') """

                        inst_register.execute(cadastro)
                        conn.commit()
                    except ValueError:
                        print("\nDigite valores numéricos! ")
                        sleep(2)

                    except:
                        print("\nErro BD")
                        sleep(2)

                    else:
                        print("\nDados cadastrados!")
                        sleep(2)

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
                        print("\nO CPF não existe.")
                        sleep(2)

                    else:
                        try:
                            opt = int(input("""
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
                            sleep(2)

                        # ALTERAR O NOME DO USUARIO
                        if opt == 1:
                            try:
                                newName = input("\nNovo nome: ").upper()

                                alter = f"""update usuariob3 set NOME = '{newName}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O CPF DO USUARIO
                        elif opt == 2:
                            try:
                                newCpf = input("\nNovo CPF: ").upper()

                                alter = f"""update usuariob3 set CPF = '{newCpf}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O EMAIL DO USUARIO
                        elif opt == 3:
                            try:
                                newEmail = input("\nNovo Email: ").upper()

                                alter = f"""update usuariob3 set EMAIL = '{newEmail}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O NASCIMENTO DO USUARIO
                        elif opt == 4:
                            try:
                                newNascimento = input("\nNova data de nascimento: ").upper()

                                alter = f"""update usuariob3 set NASCIMENTO = '{newNascimento}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O CEP DO USUARIO
                        elif opt == 5:
                            try:
                                newCep = input("\nNovo CEP: ").upper()

                                alter = f"""update usuariob3 set CEP = '{newCep}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O ENDEREÇO DO USUARIO
                        elif opt == 6:
                            try:
                                newEndereco = input("\nNovo endereço: ").upper()

                                alter = f"""update usuariob3 set ENDERECO = '{newEndereco}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O NUMERO DO USUARIO
                        elif opt == 7:
                            try:
                                newNumero = int(input("\nNovo número: "))

                                alter = f"""update usuariob3 set NUMERO = {newNumero} where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except ValueError:
                                print("\nDigite um valor numerico")
                                sleep(2)

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O COMPLEMENTO DO USUARIO
                        elif opt == 8:
                            try:
                                newComplemento = input("\nNovo complemento: ").upper()

                                alter = f"""update usuariob3 set COMPLEMENTO = '{newComplemento}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O BAIRRO DO USUARIO
                        elif opt == 9:
                            try:
                                newBairro = input("\nNovo bairro: ").upper()

                                alter = f"""update usuariob3 set BAIRRO = '{newBairro}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR A UF DO USUARIO
                        elif opt == 10:
                            try:
                                newUf = input("\nNova UF: ").upper()

                                alter = f"""update usuariob3 set UF = '{newUf}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        else:
                            print("\nDigite um  valor valido")
                            sleep(2)

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
                            sleep(2)

                        else:
                            try:
                                delete = f"""delete from usuariob3 where cpf = '{cpf}'"""
                                inst_delete.execute(delete)
                                conn.commit()

                            except:
                                print("Erro banco de dados")
                                sleep(2)

                            else:
                                print("Dados excluidos")
                                sleep(2)

                    except Exception as e:
                        print(e)

                # CASO DIGITE UM NÚMEMRO QUE NÃO EXISTA DE OPÇÃO
                else:
                    print("Digite uma opção valida")
                    sleep(2)

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
                    sleep(2)

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
                            sleep(2)
                        else:
                            print(dataDf)
                            sleep(2)
                        print("\n")

                    except Exception as e:
                        print(e)

                # CADASTRANDO ATRIBUTOS NA EMPRESA
                elif opt == 2:
                    try:
                        nome = fake.name().upper()  # input("Nome:  ")
                        cnpj = fake.cnpj().upper()  # int(input("CNPJ: "))
                        abertura = fake.random_int(1000, 9999).upper()  # input("ANO DE ABERTURA: ")


                        cadastro = f"""INSERT INTO EMPRESAB3 (NOME, CNPJ, ANOABERTURA) VALUES ('{nome}', '{cnpj}', {abertura}) """

                        inst_register.execute(cadastro)
                        conn.commit()
                    except ValueError:
                        print("Digite valores numéricos! ")
                        sleep(2)

                    except:
                        print("Erro BD")
                        sleep(2)

                    else:
                        print("Dados cadastrados!")
                        sleep(2)

                # ALTERAR DADOS DO EMPRESA
                elif opt == 3:
                    dataList = []

                    cnpj = input("Digite o CNPJ da empresa que você deseja alterar: ")

                    consult = f"""SELECT * FROM EMPRESAB3 WHERE CNPJ = '{cnpj}'"""

                    inst_consult.execute(consult)
                    data = inst_consult.fetchall()

                    for oneData in data:
                            dataList.append(oneData)

                    if len(dataList) == 0:
                        print("O CNPJ não existe.")
                        sleep(2)

                    else:
                        try:
                            opt = int(input("""
1 - NOME
2 - CNPJ
3 - ANO DE ABERTURA
Qual dado você deseja alterar? """))

                        except ValueError:
                            print("\nDigite valores numéricos! ")
                            sleep(2)

                        # ALTERAR O NOME DA EMPRESA
                        if opt == 1:
                            try:
                                newName = input("\nNovo nome: ").upper()

                                alter = f"""update EMPRESAB3 set NOME = '{newName}' where CNPJ = '{cnpj}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O CNPJ DA EMPRESA
                        elif opt == 2:
                            try:
                                newCnpj = input("\nNovo CNPJ: ").upper()

                                alter = f"""update EMPRESAB3 set CNPJ = '{newCnpj}' where CNPJ = '{cnpj}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O ANO DE ABERTURA DA EMPRESA
                        elif opt == 3:
                            try:
                                newAbertura = int(input("\nNovo ano de abertura: "))

                                alter = f"""update usuariob3 set EMAIL = {newAbertura} where cpf = '{cnpj}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except ValueError:
                                print("\nDigite um valor numérico")
                                sleep(2)

                            except:
                                print("Erro banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

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
                            sleep(2)

                        else:
                            try:
                                delete = f"""delete from EMPRESAB3 where CNPJ = '{cnpj}'"""
                                inst_delete.execute(delete)
                                conn.commit()

                            except:
                                print("Erro banco de  dados")
                                sleep(2)

                            else:
                                print("Dados excluidos")
                                sleep(2)

                    except Exception as e:
                        print(e)

                # CASO DIGITE UM NÚMEMRO QUE NÃO EXISTA DE OPÇÃO
                else:
                    print("Digite uma opção valida")
                    sleep(2)

            elif opt == 0:
                print("Volte sempre!")
                connection = False

            else:
                print("Digite uma opção valida")
                sleep(2)

    # SE O USUARIO NÃO FOR ADM
    else:
            # Menu principal com as primeiras funções
        opt = int(input("""\nBEM-VINDO!
PARA NAVEGAR ENTRE OS MENUS, DIGITE O NÚMERO DESEJADO:
1 - SIMULADOR
2 - DOCUMENTAÇÃO
3 - INFORMAÇÕES
0 - SAIR
QUAL OPÇÃO DESEJA SELECIONAR? """))

        if opt == 1:
            # Função ao executar a opção 1 do menu principal
            print("ESSE É O NOSSO SIMULADOR DE INVESTIMENTOS, PARA UTILIZA-LO, PREENCHA OS CAMPOS ABAIXO:")
            nomeEmpresa = str(input("Digite o nome da empresa: "))
            setorEmpresa = str(input("Digite o setor atuante da empresa: "))
            anoAbertura = int(input("Digite o ano de abertura: "))
            i = int(input("DIGITE 1 PARA CONTINUAR, 99 PARA VOLTAR AO INICIO OU 0 PARA SAIR: "))

            if opt == 1:
                # Caso o usuário continue, o sistema irá realizar uma consulta no banco de dados através dos dados informados acima
                print("REALIZANDO SIMULAÇÃO...")  # Simulando a consulta ao banco de dados
                sleep(2)
                print(f"""A SIMULAÇÃO COM A EMPRESA {nomeEmpresa} FOI CONCLUÍDA!
IREMOS TE RETORNAR PARA O MENU INICIAL EM ALGUNS SEGUNDOS...""")
                sleep(5)
                opt = 99  # Ao finalizar a consulta, o sistema retornara o usuário para o primeiro menu

        elif opt == 2:
            # Função ao executar a opção 2 do menu principal
            print("\nSELECIONE UM DOCUMENTO DA LISTA SUSPENSA")
            opt = int(input("""1 - DOCUMENTO 1
2 - DOCUMENTO 2
3 - DOCUMENTO 3
4 - DOCUMENTO 4
99 - VOLTAR AO MENU INICIAL
0 - SAIR
DIGITE UMA OPÇÃO: """))

            if 1 <= opt <= 4:
                # Função para seleção do ponto que será apresentado na tela para leitura
                opt = int(input(f"""\nOs principais pontos do documento {opt} são:
1 - PONTO PRINCIPAL 1
2 - PONTO PRINCIPAL 2
3 - PONTO PRINCIPAL 3
4 - PONTO PRINCIPAL 4
5 - PONTO PTINCIPAL 5 
PARA LEITURA COMPLETA DO TÓPICO SELECIONE UM ITEM, OU: 

99 - VOLTAR AO MENU INICIAL
0 - SAIR
DIGITE UMA OPÇÃO: """))

                if 1 <= opt <= 5:
                    # Apresentação completa do ponto escolhido pelo usuário
                    print(f"DESCRIÇÃO COMPLETA DO TOPICO {opt}")
                    print("AÇÃO 2 FINALIZADA, EM ALGUNS SEGUNDOS IREMOS TE RETORNAR PARA O MENI PRINCIPAL...")
                    sleep(7)
                    opt = 99

        elif opt == 3:
            # Função ao executar a opção 3 do menu principal
            opt = int(input("""\nSELECIONE O TÓPICO ABAIXO EM QUE DESEJA MAIS INFORMAÇÕES:
1 - IPO
2 - CVM
3 - TUTORIAL
4 - NOTICIAS
99 - VOLTAR AO MENU INICIAL
0 - SAIR
DIGITE UMA OPÇÃO: """))

            if 1 <= opt <= 4:
                # Função para seleção da informação do tópico que será apresentado na tela para leitura
                opt = int(input(f"""\nSELECIONE UMA INFORMAÇÃO PARA LER SOBRE O TÓPICO {opt}
1 - INFORMAÇÃO 1
2 - INFORMAÇÃO 2
3 - INFORMAÇÃO 3
4 - INFORMAÇÃO 4
5 - INFORMAÇÃO 5
99 - VOLTAR AO MENU INICIAL
0 - SAIR
DIGITE UMA OPÇÃO: """))

                if 1 <= opt <= 5:
                    # Apresentação da informação escolhida do tópico selecionado
                    print(f"\nTEXTO SOBRE A INFORMAÇÃO {opt}...")
                    print("AÇÃO 3 FINALIZADA, EM ALGUNS SEGUNDOS IREMOS TE RETORNAR PARA O MENU PRINCIPAL...")
                    sleep(7)
                    opt = 99

        elif opt == 0:
            # Finalização da utilização do sistema
            print("VOLTE SEMPRE!")

        else:
            # Tratativa de erro caso o usuário selecionar uma opção não existente
            print("DIGITE UMA OPÇÃO VÁLIDA! ")
            sleep(1)
            opt = 99
