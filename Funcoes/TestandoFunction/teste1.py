# Função para opção 1 - Funcionarios

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

def funcionario():
    # USANDO A ENTIDADE DE FUNCIONARIOS
        try:
            opt = int(input("""\nQUAL AÇÃO DESEJA EXECUTAR NOS FUNCIONARIOS?
1 - VISUALIZAR.
2 - REGISTRAR.
3 - ALTERAR.
4 - EXCLUIR.
0 - VOLTA.
QUAL OPÇÃO DESEJA SELECIONAR? """))

        except ValueError:
            print("\nDigite apenas o número da opção desejada.")
            sleep(2)

        else:
            # VISUALIZAR OS ATRIBUTOS DOS FUNCIONARIOS
            if opt == 1:
                try:
                    dataList = []

                    inst_consult.execute('SELECT * FROM FUNCIONARIOS')

                    data = inst_consult.fetchall()

                    for oneData in data:
                        dataList.append(oneData)

                    dataList = sorted(dataList)

                    dataDf = pd.DataFrame.from_records(dataList,
                                                       columns=['ID', 'ID_CARGO', 'CPF', 'NOME', 'SALARIO',
                                                                'IDADE'], index='ID')
                    if (dataDf.empty):
                        print("\nNão há registros")
                        sleep(2)
                    else:
                        print(dataDf)
                        sleep(2)
                    print("\n")

                except Exception as e:
                    print(e)
                    sleep(2)

            # CADASTRANDO ATRIBUTOS NOS FUNCIONARIOS
            elif opt == 2:
                try:
                    funcionario_id = int(input("\nID funcionarios: "))
                    cargo_id = int(input("Id do cargo: "))
                    funcionario_cpf = int(input("CPF: "))
                    funcionario_nome = input("Nome: ").upper()
                    funcionario_salario = float(input("Salário: "))
                    funcionario_idade = int(input("Idade: "))

                    register = f"""INSERT INTO FUNCIONARIOS VALUES ({funcionario_id}, {cargo_id}, {funcionario_cpf},
                                '{funcionario_nome}', {funcionario_salario}, {funcionario_idade})"""

                    inst_register.execute(register)
                    conn.commit()

                except ValueError:
                    print("\nDigite um valor numérico.")

                except:
                    print("\nErro banco de dados")

                else:
                    print("\nDados cadastrados")

            # ALTERAR DADOS DOS FUNCIONARIOS
            elif opt == 3:
                dataList = []

                funcionario_id = input("\nDigite o ID do funcionario que você deseja alterar: ")

                consult = f"""SELECT * FROM FUNCIONARIOS WHERE funcionario_id = {funcionario_id}"""

                inst_consult.execute(consult)
                data = inst_consult.fetchall()

                for oneData in data:
                    dataList.append(oneData)

                if len(dataList) == 0:
                    print("\nO funcionario não existe.")
                    sleep(2)

                else:
                    try:
                        opt = int(input("""
1 - Funcionario ID
2 - Cargo ID
3 - CPF
4 - NOME
5 - SALÁRIO
6 - IDADE
Qual dado você deseja alterar? """))

                    except ValueError:
                        print("\nDigite valores numéricos! ")
                        sleep(2)

                    # ALTERAR O ID DO FUNCIONARIO
                    if opt == 1:
                        try:
                            newFuncionarioId = int(input("\nNovo ID funcionario: "))

                            alter = f"""update FUNCIONARIOS set funcionario_id = {newFuncionarioId} where funcionario_id = {funcionario_id}"""

                            inst_update.execute(alter)
                            conn.commit()

                        except ValueError:
                            print("\nDigite apenas valores numéricos")

                        except:
                            print("\nERRO banco de dados")
                            sleep(2)

                        else:
                            print("\nAtualização realizada!")
                            sleep(2)

                    # ALTERAR O ID DO CARGO RELACIONADO AO FUNCIONARIO
                    elif opt == 2:
                        try:
                            newCargoId = int(input("\nNovo ID cargo: "))

                            alter = f"""update FUNCIONARIOS set cargo_id = {newCargoId} where funcionario_id = {funcionario_id}"""

                            inst_update.execute(alter)
                            conn.commit()

                        except ValueError:
                            print("\nDigite apenas valores numéricos")

                        except:
                            print("\nERRO banco de dados")
                            sleep(2)

                        else:
                            print("\nAtualização realizada!")
                            sleep(2)

                    # ALTERAR O CPF DO FUNCIONARIO
                    elif opt == 3:
                        try:
                            newFuncionarioCpf = int(input("\nNovo CPF: "))

                            alter = f"""update FUNCIONARIOS set FUNCIONARIO_CPF = {newFuncionarioCpf} where funcionario_id = {funcionario_id}"""

                            inst_update.execute(alter)
                            conn.commit()

                        except ValueError:
                            print("\nDigite apenas valores numéricos")

                        except:
                            print("\nERRO banco de dados")
                            sleep(2)

                        else:
                            print("\nAtualização realizada!")
                            sleep(2)

                    # ALTERAR O NOME DO FUNCIONARIO
                    elif opt == 4:
                        try:
                            newFuncionarioNome = input("\nNovo nome: ").upper()

                            alter = f"""update FUNCIONARIOS set FUNCIONARIO_NOME = '{newFuncionarioNome}' where funcionario_id = {funcionario_id}"""

                            inst_update.execute(alter)
                            conn.commit()

                        except:
                            print("\nERRO banco de dados")
                            sleep(2)

                        else:
                            print("\nAtualização realizada!")
                            sleep(2)

                    # ALTERAR O SALARIO DO FUNCIONARIO
                    elif opt == 5:
                        try:
                            newFuncionarioSalario = float(input("\nNovo salario: "))

                            alter = f"""update FUNCIONARIOS set FUNCIONARIO_SALARIO = {newFuncionarioSalario} where funcionario_id = {funcionario_id}"""

                            inst_update.execute(alter)
                            conn.commit()

                        except ValueError:
                            print("\nDigite apenas valores numéricos")

                        except:
                            print("\nERRO banco de dados")
                            sleep(2)

                        else:
                            print("\nAtualização realizada!")
                            sleep(2)

                    # ALTERAR A IDADE DO FUNCIONARIO
                    elif opt == 6:
                        try:
                            newFuncionarioIdade = int(input("\nNova idade: "))

                            alter = f"""update FUNCIONARIOS set FUNCIONARIO_IDADE = {newFuncionarioIdade} where funcionario_id = {funcionario_id}"""

                            inst_update.execute(alter)
                            conn.commit()

                        except ValueError:
                            print("\nDigite apenas valores numéricos")

                        except:
                            print("\nERRO banco de dados")
                            sleep(2)

                        else:
                            print("\nAtualização realizada!")
                            sleep(2)

                    # SAIR
                    elif opt == 0:
                        connection = False
                        sleep(2)

                    # OPÇÕES INVALIDAS
                    else:
                        print("\nDigite uma  opção válida!")
                        sleep(2)

            # EXCLUIR DADOS DOS FUNCIONARIOS
            elif opt == 4:
                try:
                    dataList = []
                    funcionario_id = int(input("\nDigiteo ID do funncionario que deseja deletar: "))

                    consult = f"""SELECT * FROM FUNCIONARIOS WHERE funcionario_id = {funcionario_id}"""

                    inst_consult.execute(consult)
                    data = inst_consult.fetchall()

                    for oneData in data:
                        dataList.append(data)

                    if len(dataList) == 0:
                        print("\nO ID do funncionario digitado não existe")
                        sleep(2)

                    else:
                        try:
                            delete = f"""DELETE FROM FUNCIONARIOS WHERE funcionario_id = {funcionario_id}"""
                            inst_delete.execute(delete)
                            conn.commit()

                        except:
                            print("\nErro banco de dados")
                            sleep(2)

                        else:
                            print("\nDados excluidos")
                            sleep(2)

                except Exception as e:
                    print(e)

            # VOLTAR
            elif opt == 0:
                print("\nMenu inicial")
                sleep(1)

            else:
                print("\nDigite uma opção válida.")
                sleep(1)