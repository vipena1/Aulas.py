# Função para opção 2 - Cargos

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

def cargo():
    # USANDO A ENTIDADE DE CARGOS

    try:
        opt = int(input("""\nQUAL AÇÃO DESEJA EXECUTAR NOS CARGOS?
1 - VISUALIZAR.
2 - REGISTRAR.
3 - ALTERAR.
4 - EXCLUIR.
0 - VOLTAR.
QUAL OPÇÃO DESEJA SELECIONAR? """))

    except ValueError:
        print("\nDigite apenas o número da opção desejada.")
        sleep(2)

    else:
        # VISUALIZAR OS ATRIBUTOS DOS CARGOS
        if opt == 1:
            try:
                dataList = []

                inst_consult.execute('SELECT * FROM CARGOS')

                data = inst_consult.fetchall()

                for oneData in data:
                    dataList.append(oneData)

                dataList = sorted(dataList)

                dataDf = pd.DataFrame.from_records(dataList, columns=['ID', 'DESCRIÇÃO', 'DEPARTAMENTO'], index='ID')
                if (dataDf.empty):
                    print("\nNão há registros")
                    sleep(2)
                else:
                    print(dataDf)
                    sleep(2)
                print("\n")

            except Exception as e:
                print(e)

        # CADASTRANDO ATRIBUTOS NOS CAGOS
        elif opt == 2:
            try:
                cargo_id = int(input("ID:  "))
                cargo_descricao = input("Descrição: ").upper()
                cargo_departamento = input("Departamento: ").upper()

                register = f"""INSERT INTO CARGOS VALUES ({cargo_id}, '{cargo_descricao}', '{cargo_departamento}')"""

                inst_register.execute(register)
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

        # ALTERAR DADOS DOS CARGOS
        elif opt == 3:
            dataList = []

            cargo_id = int(input("Digite o ID do cargo que você deseja alterar: "))

            consult = f"""SELECT * FROM CARGOS WHERE CARGO_ID = {cargo_id}"""

            inst_consult.execute(consult)
            data = inst_consult.fetchall()

            for oneData in data:
                dataList.append(oneData)

            if len(dataList) == 0:
                print("O ID não existe.")
                sleep(2)

            else:
                try:
                    opt = int(input("""
1 - ID
2 - DESCRIÇÃO
3 - DEPARTAMENTO
Qual dado você deseja alterar? """))

                except ValueError:
                    print("\nDigite valores numéricos! ")
                    sleep(2)

                else:
                    # ALTERAR O ID DO CARGO
                    if opt == 1:
                        try:
                            newCargoId = int(input("\nNovo ID: "))

                            alter = f"""update CARGOS set CARGO_ID = {newCargoId} where CARGO_ID = {cargo_id}"""

                            inst_update.execute(alter)
                            conn.commit()

                        except ValueError:
                            print("\nDigite valores numéricos")
                            sleep(2)

                        except:
                            print("Erro banco de dados")
                            sleep(2)

                        else:
                            print("Atualização realizada com sucesso!")
                            sleep(2)

                    # ALTERAR A DESCRIÇÃO DO CARGO
                    elif opt == 2:
                        try:
                            newDescricao = input("\nNova descrição do cargo: ").upper()

                            alter = f"""update CARGOS set CARGO_DESCRICAO = '{newDescricao}' where CARGO_ID = {cargo_id}"""

                            inst_update.execute(alter)
                            conn.commit()

                        except:
                            print("Erro banco de dados")
                            sleep(2)

                        else:
                            print("Atualização realizada com sucesso!")
                            sleep(2)

                    # ALTERAR O DEPARTAMENTO DO CARGO
                    elif opt == 3:
                        try:
                            newDepartamento = input("\nNova departamento do cargo: ").upper()

                            alter = f"""update CARGOS set CARGO_DEPARTAMENTO = '{newDepartamento}' where CARGO_ID = {cargo_id}"""

                            inst_update.execute(alter)
                            conn.commit()

                        except:
                            print("Erro banco de dados")
                            sleep(2)

                        else:
                            print("Atualização realizada com sucesso!")
                            sleep(2)

        # EXCLUIR DADOS DOS CARGOS
        elif opt == 4:
            try:
                dataList = []

                cargo_id = int(input("\nDigite o ID do cargo que deseja excluir: "))

                consult = f"""SELECT * FROM CARGOS WHERE CARGO_ID = {cargo_id}"""

                inst_consult.execute(consult)
                data = inst_consult.fetchall()

                for oneData in data:
                    dataList.append(data)

                if len(dataList) == 0:
                    print("\nO ID digitado não existe")
                    sleep(2)

                else:
                    try:
                        delete = f"""delete from CARGOS where CARGO_ID = {cargo_id}"""
                        inst_delete.execute(delete)
                        conn.commit()

                    except:
                        print("\nErro banco de  dados")
                        sleep(2)

                    else:
                        print("\nDados excluidos")
                        sleep(2)

            except Exception as e:
                print(e)

        elif opt == 0:
            print("Menu inicial.")
            sleep(1)

        else:
            print("Digite uma opção válida.")
