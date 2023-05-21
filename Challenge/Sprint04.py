"""Integração do programa Python com a mesma base de dados que o sistema web tem;

 O programa deve ter ao menos 2 menus (telas) com interação com BD;

 Cada menu deve ler (SELECT) informações do BD; ? Cada menu deve escrever (INSERT, UPDATE ou DELETE) no BD;

 Todas as informações alteradas através do programa python, devem ser refletidas no sistema web. """

import oracledb as orcl
import pandas as pd
from time import sleep

try:
    # Abrindo conexão com o banco
    dnStr = orcl.makedsn("oracle.fiap.com.br", "1521", "ORCL")
    conn = orcl.connect(user="RM97032", password="fiap23", dsn=dnStr)

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

                        inst_consult.execute('SELECT * FROM USUARIO')

                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(oneData)

                        dataList = sorted(dataList)

                        dataDf = pd.DataFrame.from_records(dataList,
                                                           columns=['NOME', 'EMAIL', 'CEP', 'RUA', 'BAIRRO', 'UF',
                                                                    'CPF', 'SENHA', 'DT NASCIMENTO', 'CELULAR'],
                                                           index='CPF')
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
                        nome = input("NOME:  ").upper()
                        email = input("EMAIL: ").upper()
                        cep = int(input("CEP: "))
                        rua = input("RUA: ").upper()
                        bairro = input("BAIRRO: ").upper()
                        uf = input("UF: ").upper()
                        cpf = input("CPF: ")
                        senha = input("SENHA: ")

                        try:
                            dtNacimento = input("DATA DE NASCIMENTO(DD/MM/AA): ")
                            # Padronização de data para banco de dados
                            listaData = dtNacimento.split("/")

                            listaMes = ["jan", "feb", "mar",
                                        "apr", "may", "jun",
                                        "jul", "aug", "sep",
                                        "oct", "nov", "dec"]

                            textoMes = listaMes[int(listaData[1]) - 1]
                            dtNacimento = f'{listaData[0]}-{textoMes}-{listaData[2]}'
                        except:
                            print("Digite um mês válido.")

                        celular = int(input("N° CELULAR: "))

                        cadastro = f"""INSERT INTO USUARIO VALUES ('{nome}', '{email}', {cep}, '{rua}', '{bairro}', '{uf}', '{cpf}', '{senha}', '{dtNacimento}', {celular}) """

                        inst_register.execute(cadastro)
                        conn.commit()
                    except ValueError:
                        print("\nDigite valores numéricos! ")
                        sleep(2)

                    except Exception as e:
                        print(e)
                        sleep(2)

                    else:
                        print("\nDados cadastrados!")
                        sleep(2)

                # ALTERAR DADOS DO USUÁRIO
                elif opt == 3:
                    dataList = []

                    cpf = input("Digite o CPF do usuário que você deseja alterar: ")

                    consult = f"""SELECT * FROM USUARIO WHERE CPF = '{cpf}'"""

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
2 - EMAIL
3 - CEP
4 - RUA
5 - BAIRRO
6 - UF
7 - CPF
8 - SENHA
9 - DATA DE NASCIMENTO
10 - CELULAR

Qual dado você deseja alterar? """))

                        except ValueError:
                            print("\nDigite valores numéricos! ")
                            sleep(2)

                        # ALTERAR O NOME DO USUARIO
                        if opt == 1:
                            try:
                                newName = input("\nNovo nome: ").upper()

                                alter = f"""update USUARIO set NOME_USUARIO = '{newName}' where CPF = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O E-MAIL DO USUARIO
                        elif opt == 2:
                            try:
                                newEmail = input("\nNovo E-MAIL: ").upper()

                                alter = f"""update USUARIO set EMAIL = '{newEmail}' where CPF = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O CEP DO USUARIO
                        elif opt == 3:
                            try:
                                newCep = int(input("\nNovo CEP: "))

                                alter = f"""update USUARIO set CEP = {newCep} where CPF = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except ValueError:
                                print("\nDigite um valor numérico.")
                                sleep(2)

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR A RUA DO USUARIO
                        elif opt == 4:
                            try:
                                newRua = input("\nNova rua: ").upper()

                                alter = f"""update USUARIO set RUA = '{newRua}' where CPF = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O BAIRRO DO USUARIO
                        elif opt == 5:
                            try:
                                newBairro = input("\nNovo Bairro: ").upper()

                                alter = f"""update USUARIO set BAIRRO = '{newBairro}' where CPF = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O UF DO USUARIO
                        elif opt == 6:
                            try:
                                newUf = input("\nNova UF: ").upper()

                                alter = f"""update USUARIO set UF = '{newUf}' where CPF = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O CPF DO USUARIO
                        elif opt == 7:
                            try:
                                newCpf = int(input("\nNovo CPF: "))

                                alter = f"""update USUARIO set CPF = '{newCpf}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR A SENHA DO USUARIO
                        elif opt == 8:
                            try:
                                newSenha = input("\nNova senha: ")

                                alter = f"""update USUARIO set SENHA = '{newSenha}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR A DATA DE NASCIMENTO DO USUARIO
                        elif opt == 9:
                            try:
                                newDtNascimento = input("\nNova data de nascimento (DD/MM/AA): ")

                                try:
                                    # Padronização de data para banco de dados
                                    listaData = newDtNascimento.split("/")

                                    listaMes = ["jan", "feb", "mar",
                                                "apr", "may", "jun",
                                                "jul", "aug", "sep",
                                                "oct", "nov", "dec"]

                                    textoMes = listaMes[int(listaData[1]) - 1]
                                    newDtNascimento = f'{listaData[0]}-{textoMes}-{listaData[2]}'
                                except:
                                    print("Insira uma data válida.")

                                alter = f"""update USUARIO set DATA_NASC = '{newDtNascimento}' where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O CELULAR DO USUARIO
                        elif opt == 10:
                            try:
                                newCel = int(input("\nNovo n° celular: "))

                                alter = f"""update USUARIO set CEL = {newCel} where cpf = '{cpf}'"""

                                inst_update.execute(alter)
                                conn.commit()

                            except ValueError:
                                print("\nDigite valores numéricos")
                                sleep(2)

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

                        consult = f"""SELECT * FROM USUARIO WHERE cpf = '{cpf}'"""

                        inst_consult.execute(consult)
                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(data)

                        if len(dataList) == 0:
                            print("O cpf digitado não existe")
                            sleep(2)

                        else:
                            try:
                                delete = f"""delete from USUARIO where cpf = '{cpf}'"""
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

                        inst_consult.execute('SELECT * FROM EMPRESA')

                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(oneData)

                        dataList = sorted(dataList)

                        dataDf = pd.DataFrame.from_records(dataList,
                                                           columns=['CNPJ', 'NOME', 'SETOR', 'ANO DE ABERTURA',
                                                                    'PRIMEIRO SEMESTRE', 'SEGUNDO SEMESTRE',
                                                                    'TERCEIRO SEMESTRE', 'QUARTO SEMESTRE'],
                                                           index='CNPJ')
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
                        cnpj = int(input("CNPJ: "))
                        nome = input("Nome: ").upper()
                        setor = input("Setor: ").upper()
                        anoAbertura = input("ANO DE ABERTURA: ")
                        priTrimestre = float(input("Primeiro semestre: "))
                        segTrimestre = float(input("Segundo semestre: "))
                        terTrimestre = float(input("Terceiro semestre: "))
                        quaTrimestre = float(input("Quarto semestre: "))

                        cadastro = f"""INSERT INTO EMPRESA VALUES ({cnpj}, '{nome}', '{setor}', '{anoAbertura}', {priTrimestre}, {segTrimestre}, {terTrimestre}, {quaTrimestre})"""

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

                    try:
                        cnpj = int(input("Digite o CNPJ da empresa que você deseja alterar: "))

                        consult = f"""SELECT * FROM EMPRESA WHERE CNPJ = {cnpj}"""

                        inst_consult.execute(consult)
                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(oneData)

                        if len(dataList) == 0:
                            print("O CNPJ não existe.")
                            sleep(2)

                    except ValueError:
                        print("\nDigite valores numéricos.")

                    else:
                        try:
                            opt = int(input("""
1 - CNPJ
2 - NOME
3 - SETOR
4 - ANO DE ABERTURA
5 - PRIMEIRO TRIMESTRE
6 - SEGUNDO TRIMESTRE
7 - TERCEIRO TRIMESTRE
8 - QUARTO TRIMESTRE
Qual dado você deseja alterar? """))

                        except ValueError:
                            print("\nDigite valores numéricos! ")
                            sleep(2)

                        # ALTERAR O CNPJ DA EMPRESA
                        if opt == 1:
                            try:
                                newCnpj = int(input("\nNovo CNPJ: "))

                                alter = f"""update EMPRESA set CNPJ = {newCnpj} where CNPJ = {cnpj}"""

                                inst_update.execute(alter)
                                conn.commit()

                            except ValueError:
                                print("Digite valores numéricos.")

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O NOME DA EMPRESA
                        elif opt == 2:
                            try:
                                newNome = input("\nNovo nome: ").upper()

                                alter = f"""update EMPRESA set NOME_EMPRESA = '{newNome}' where CNPJ = {cnpj}"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O SETOR DA EMPRESA
                        elif opt == 3:
                            try:
                                newSetor = input("\nNovo setor: ")

                                alter = f"""update EMPRESA set SETOR = '{newSetor}' where cnpj = {cnpj}"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("Erro banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O ANO DE ABERTURA DA EMPRESA
                        elif opt == 4:
                            try:
                                newAnoAbertura = input("\nNovo ano de abertura: ")

                                alter = f"""update EMPRESA set ANO_ABERTURA = {newAnoAbertura} where cnpj = {cnpj}"""

                                inst_update.execute(alter)
                                conn.commit()

                            except:
                                print("Erro banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O PRIMEIRO SEMESTRE DA EMPRESA
                        elif opt == 5:
                            try:
                                newPriSemestre = float(input("\nNovo primeiro semestre: "))

                                alter = f"""update EMPRESA set PRIMEIRO_TRIMESTRE = {newPriSemestre} where CNPJ = {cnpj}"""

                                inst_update.execute(alter)
                                conn.commit()

                            except ValueError:
                                print("Digite valores numéricos.")

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O SEGUNDO SEMESTRE DA EMPRESA
                        elif opt == 6:
                            try:
                                newSegSemestre = float(input("\nNovo segundo semestre: "))

                                alter = f"""update EMPRESA set SEGUNDO_TRIMESTRE = {newSegSemestre} where CNPJ = {cnpj}"""

                                inst_update.execute(alter)
                                conn.commit()

                            except ValueError:
                                print("Digite valores numéricos.")

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")
                                sleep(2)

                        # ALTERAR O TERCEIRO SEMESTRE DA EMPRESA
                        elif opt == 7:
                            try:
                                newTerSemestre = float(input("\nNovo terceiro semestre: "))

                                alter = f"""update EMPRESA set TERCEIRO_TRIMESTRE = {newTerSemestre} where CNPJ = {cnpj}"""

                                inst_update.execute(alter)
                                conn.commit()

                            except ValueError:
                                print("Digite valores numéricos.")

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")

                        # ALTERAR O QUARTO SEMESTRE DA EMPRESA
                        elif opt == 8:
                            try:
                                newQuaSemestre = float(input("\nNovo quarto semestre: "))

                                alter = f"""update EMPRESA set QUARTO_TRIMESTRE = {newQuaSemestre} where CNPJ = {cnpj}"""

                                inst_update.execute(alter)
                                conn.commit()

                            except ValueError:
                                print("Digite valores numéricos.")

                            except:
                                print("\nERRO banco de dados")
                                sleep(2)

                            else:
                                print("\nAtualização realizada!")

                # EXCLUIR DADOS DA EMPRESA
                elif opt == 4:
                    try:
                        dataList = []

                        cnpj = int(input("\nDigite o CNPJ da empresa que deseja excluir: "))

                        consult = f"""SELECT * FROM EMPRESA WHERE CNPJ = {cnpj}"""

                        inst_consult.execute(consult)
                        data = inst_consult.fetchall()

                        for oneData in data:
                            dataList.append(data)

                        if len(dataList) == 0:
                            print("O CNPJ digitado não existe")
                            sleep(2)

                        else:
                            try:
                                delete = f"""delete from EMPRESA where CNPJ = {cnpj}"""
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
            connection = False

        else:
            # Tratativa de erro caso o usuário selecionar uma opção não existente
            print("DIGITE UMA OPÇÃO VÁLIDA! ")
            sleep(1)
            opt = 99
