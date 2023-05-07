""" Desenvolvimento em Python de um programa que será o acesso ADM do sistema;

 Esse programa deve ter a responsabilidade de ter no mínimo 2 telas (menus) que não existirão no frontend web, mas que serão necessárias para complementar os requisitos funcionais;

As telas devem ter todas as validações necessárias e obtenção de todas as informações (campos), conforme requisitos funcionais;

Além disso, todas as informações solicitadas nessas telas, devem ser coerentes com os campos do banco de dados."""

from time import sleep

listaUsuario = [['João', "Souza", "joao23@gmail.com", "jsouza", "Qualquercoisa1!", 18, 11933334444, "09424345"],
                ["Maria", "Silva", "mariazinha@hotmail.com", "marizinha", "Qualquercoisa2@", 25, 11911112222, "08823468"],
                ["José", "Fernandes", "josefernandes1@gmail.com", "josefer", "Qualquercoisa3#", 30, 11955556666, "23794375"]]

listaEmpresa = [["Nubank", "Financeiro", 2013],
                ["Magazine Luiza", "Varejo", 1957],
                ["Vale", "Mineradora", 1942]]

i = 99
user = input("DIGITE O USUÁRIO: ")
password = input("DIGITE A SENHA: ")

while i != 0:
    # O menu seguinte só será acessado com a senha de administrador
    if user == "ADM" and password == "ADMIN123":
        try:
            i = int(input("""\nMenu de administrador.
1 - ALTERAR DADOS DE USUÁRIO.
2 - ALTERAR DADOS DE EMPRESAS.
0 - SAIR
DIGITE A OPÇÃO DESEJADA: """))

            if i == 1:  # Menu de ações para realizar com os dados de usuários.
                i = int(input("""\nQUAL AÇÃO DESEJA EXECUTAR NO USUÁRIO?
1 - VISUALIZAR.
2 - ALTERAR.
3 - EXCLUIR.
QUAL OPÇÃO DESEJA SELECIONAR? """))



                if i == 1:  # Apenas para visualização dos usuários cadastrados.
                    print("\nLISTA DE USUÁRIOS: ")
                    for x in range(0, len(listaUsuario)):
                        print(f"{x + 1} - {listaUsuario[x][0]}")

                    i = int(input("QUAL USUÁRIO DESEJA VISUALIZAR? "))
                    print(f"""\nUSUÁRIO {i} SELECIONADO.
NOME: {listaUsuario[i - 1][0]}
SOBRE NOME: {listaUsuario[i - 1][1]}
E-MAIL: {listaUsuario[i - 1][2]}
USERNAME: {listaUsuario[i - 1][3]}
SENHA: {listaUsuario[i - 1][4]}
IDADE: {listaUsuario[i - 1][5]}
CELULAR: {listaUsuario[i - 1][6]}
CEP: {listaUsuario[i - 1][7]}""")
                    sleep(3)


                elif i == 2:  # Alteração de dados do usuário
                    print("\nLISTA DE USUÁRIOS:")
                    for x in range(0, len(listaUsuario)):
                        print(f"""{x + 1} - {listaUsuario[x][0]}""")
                    i = int(input("QUAL USUÁRIO DESEJA ALTERAR? "))

                    i2 = int(input("""\nABAIXO ESTÁ A LISTA DE INFORMAÇÕES DOS USUÁRIOS:
1 - NOME
2 - SOBRE NOME
3 - E-MAIL
4 - USERNAME
5 - SENHA
6 - IDADE
7 - CELULAR
8 - CEP
QUAL INFORMAÇÃO DESEJA ALTERAR?"""))

                    listaUsuario[i - 1][i2 - 1] = input("QUAL INFORMAÇÃO DESEJA PREENCHER? ")
                    print("\nAlterado com sucesso!")
                    sleep(2)

                elif i == 3:  # Excluir usuário

                    for x in range(0, len(listaUsuario)):
                        print("\nLISTA DE USUÁRIOS:")
                        print(f"{x + 1} - {listaUsuario[x][0]}")
                    i = int(input("QUAL USUÁRIO DESEJA EXCLUIR? "))

                    del listaUsuario[i - 1]
                    print("\nUSUÁRIO REMOVIDO DO SISTEMA.")
                    sleep(2)

            elif i == 2:  # Menu de ações para realizar com os dados das empresas.
                i = int(input("""\nQUAL AÇÃO DESEJA EXECUTAR NA EMPRESA?
1 - VISUALIZAR.
2 - ALTERAR.
3 - EXCLUIR.
QUAL OPÇÃO DESEJA SELECIONAR? """))

                if i == 1:  # Apenas para visualização das empresas cadastrados.
                    print("\nLISTA DE EMPRESAS: ")
                    for x in range(0, len(listaEmpresa)):
                        print(f"{x + 1} - {listaEmpresa[x][0]}")
                    i = int(input("QUAL EMPRESA DESEJA VISUALIZAR? "))

                    print(f"""\nEMPRESA {i} SELECIONADA.
NOME: {listaEmpresa[i - 1][0]}
SETOR: {listaEmpresa[i - 1][1]}
ANO DE ABERTURA: {listaEmpresa[i - 1][2]}""")
                    sleep(3)

                elif i == 2:  # Alteração de dados da empresa
                    print("\nLISTA DE EMPRESAS: ")
                    for x in range(0, len(listaEmpresa)):
                        print(f"""{x + 1} - {listaEmpresa[x][0]}""")
                    i = int(input("QUAL EMPRESA DESEJA ALTERAR? "))

                    i2 = int(input("""\nABAIXO ESTÁ A LISTA DE INFORMAÇÕES DAS EMPRESAS:
1 - NOME
2 - SETOR
3 - ANO DE ABERTURA
QUAL INFORMAÇÃO DESEJA ALTERAR?"""))

                    listaEmpresa[i - 1][i2 - 1] = input("\nQUAL INFORMAÇÃO DESEJA PREENCHER? ")
                    print("\nALTERADO COM SUCESSO!")
                    sleep(2)

                elif i == 3:  # Excluir empresa
                    print("\nLISTA DE EMPRESAS:")
                    for x in range(0, len(listaEmpresa)):
                        print(f"{x + 1} - {listaEmpresa[x][0]}")
                    i = int(input("QUAL EMPRESA DESEJA EXCLUIR? "))

                    del listaEmpresa[i - 1]
                    print("\nEMPRESA REMOVIDA DO SISTEMA.")
                    sleep(2)

            elif i == 0:  # Saida
                print("\nVOLTE SEMPRE!")

            else:
                print("\nDIGITE UMA OPÇÃO VALIDA!")

        except ValueError:
            print("\nINSIRA APENAS UM VALOR NUMERICO.")

        finally:
            sleep(1)
            print("\nOPERAÇÃO FINALIZADA")

    else:

        if i == 99:
            # Menu principal com as primeiras funções
            i = int(input("""\nBEM-VINDO!
PARA NAVEGAR ENTRE OS MENUS, DIGITE O NÚMERO DESEJADO:
1 - SIMULADOR
2 - DOCUMENTAÇÃO
3 - INFORMAÇÕES
0 - SAIR
QUAL OPÇÃO DESEJA SELECIONAR? """))

        if i == 1:
            # Função ao executar a opção 1 do menu principal
            print("ESSE É O NOSSO SIMULADOR DE INVESTIMENTOS, PARA UTILIZA-LO, PREENCHA OS CAMPOS ABAIXO:")
            nomeEmpresa = str(input("Digite o nome da empresa: "))
            setorEmpresa = str(input("Digite o setor atuante da empresa: "))
            anoAbertura = int(input("Digite o ano de abertura: "))
            i = int(input("DIGITE 1 PARA CONTINUAR, 99 PARA VOLTAR AO INICIO OU 0 PARA SAIR: "))

            if i == 1:
                # Caso o usuário continue, o sistema irá realizar uma consulta no banco de dados através dos dados informados acima
                print("REALIZANDO SIMULAÇÃO...")  # Simulando a consulta ao banco de dados
                sleep(2)
                print(f"""A SIMULAÇÃO COM A EMPRESA {nomeEmpresa} FOI CONCLUÍDA!
IREMOS TE RETORNAR PARA O MENU INICIAL EM ALGUNS SEGUNDOS...""")
                sleep(5)
                i = 99  # Ao finalizar a consulta, o sistema retornara o usuário para o primeiro menu

        elif i == 2:
            # Função ao executar a opção 2 do menu principal
            print("\nSELECIONE UM DOCUMENTO DA LISTA SUSPENSA")
            i = int(input("""1 - DOCUMENTO 1
2 - DOCUMENTO 2
3 - DOCUMENTO 3
4 - DOCUMENTO 4
99 - VOLTAR AO MENU INICIAL
0 - SAIR
DIGITE UMA OPÇÃO: """))

            if 1 <= i <= 4:
                # Função para seleção do ponto que será apresentado na tela para leitura
                i = int(input(f"""\nOs principais pontos do documento {i} são:
1 - PONTO PRINCIPAL 1
2 - PONTO PRINCIPAL 2
3 - PONTO PRINCIPAL 3
4 - PONTO PRINCIPAL 4
5 - PONTO PTINCIPAL 5 
PARA LEITURA COMPLETA DO TÓPICO SELECIONE UM ITEM, OU: 

99 - VOLTAR AO MENU INICIAL
0 - SAIR
DIGITE UMA OPÇÃO: """))

                if 1 <= i <= 5:
                    # Apresentação completa do ponto escolhido pelo usuário
                    print(f"DESCRIÇÃO COMPLETA DO TOPICO {i}")
                    print("AÇÃO 2 FINALIZADA, EM ALGUNS SEGUNDOS IREMOS TE RETORNAR PARA O MENI PRINCIPAL...")
                    sleep(7)
                    i = 99

        elif i == 3:
            # Função ao executar a opção 3 do menu principal
            i = int(input("""\nSELECIONE O TÓPICO ABAIXO EM QUE DESEJA MAIS INFORMAÇÕES:
1 - IPO
2 - CVM
3 - TUTORIAL
4 - NOTICIAS
99 - VOLTAR AO MENU INICIAL
0 - SAIR
DIGITE UMA OPÇÃO: """))

            if 1 <= i <= 4:
                # Função para seleção da informação do tópico que será apresentado na tela para leitura
                i = int(input(f"""\nSELECIONE UMA INFORMAÇÃO PARA LER SOBRE O TÓPICO {i}
1 - INFORMAÇÃO 1
2 - INFORMAÇÃO 2
3 - INFORMAÇÃO 3
4 - INFORMAÇÃO 4
5 - INFORMAÇÃO 5
99 - VOLTAR AO MENU INICIAL
0 - SAIR
DIGITE UMA OPÇÃO: """))

                if 1 <= i <= 5:
                    # Apresentação da informação escolhida do tópico selecionado
                    print(f"\nTEXTO SOBRE A INFORMAÇÃO {i}...")
                    print("AÇÃO 3 FINALIZADA, EM ALGUNS SEGUNDOS IREMOS TE RETORNAR PARA O MENU PRINCIPAL...")
                    sleep(7)
                    i = 99

        elif i == 0:
            # Finalização da utilização do sistema
            print("VOLTE SEMPRE!")

        else:
            # Tratativa de erro caso o usuário selecionar uma opção não existente
            print("DIGITE UMA OPÇÃO VÁLIDA! ")
            sleep(1)
            i = 99
