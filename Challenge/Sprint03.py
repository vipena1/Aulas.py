""" Desenvolvimento em Python de um programa que será o acesso ADM do sistema;

 Esse programa deve ter a responsabilidade de ter no mínimo 2 telas (menus) que não existirão no frontend web, mas que serão necessárias para complementar os requisitos funcionais;

As telas devem ter todas as validações necessárias e obtenção de todas as informações (campos), conforme requisitos funcionais;

Além disso, todas as informações solicitadas nessas telas, devem ser coerentes com os campos do banco de dados."""

from time import sleep

listaUsuario = [['João', 'Silva', 18], ["Maria", "Souza", 25], ["José", "Fernandes", 30]]

i = 99
user = input("Digite o usuário: ")
password = input("Digite a senha: ")

while i != 0:
    # Menu utilizado para login de administrador
    if user == "ADM" and password == "ADMIN123":
        try:
            i = int(input("""\nMenu de administrador.
1 - Alterar dados de usuário.
2 - Alterar dados de empresas.
0 - SAIR
Digite a opção desejada: """))

            if i == 1:  # Menu de ações para realizar com os dados de usuários.
                i = int(input("""\nQual ação deseja executar no usuario?
1 - VISUALIZAR.
2 - ALTERAR.
3 - EXCLUIR.

QUAL OPÇÃO DESEJA SELECIONAR? """))

                if i == 1:  # Apenas para vizualização dos usuários cadastrados.
                    print("LISTA DE USUÁRIOS: ")
                    for x in range(0, len(listaUsuario)):
                        print(f"{x + 1} - {listaUsuario[x][0]}")

                    i = int(input("QUAL USUÁRIO DESEJA VISUALIZAR? "))

                    # i = int(input(f"""\nLISTA DE USUÁRIOS:
                    # 1 - {listaUsuario[0][0]}
                    # 2 - {listaUsuario[1][0]}
                    # 3 - {listaUsuario[2][0]}
                    # QUAL USUÁRIO DESEJA SELECIONAR? """))

                    print(f"""\nUSUÁRIO {i} SELECIONADO.
NOME: {listaUsuario[i - 1][0]}.
SOBRE NOME: {listaUsuario[i - 1][1]}
IDADE: {listaUsuario[i - 1][2]}""")
                    sleep(3)

                elif i == 2:  # Alteração de dados do usuário

                    for x in range(0, len(listaUsuario)):
                        print(f"{x + 1} - {listaUsuario[x][0]}")
                    i = int(input("QUAL USUÁRIO DESEJA ALTERAR? "))

                    i2 = int(input("""\nABAIXO ESTÁ A LISTA DE INFORMAÇÕES DOS USUÁRIOS:
1 - NOME
2 - SOBRE NOME
3 - IDADE
QUAL INFORMAÇÃO DESEJA ALTERAR?"""))

                    listaUsuario[i - 1][i2 - 1] = input("QUAL INFORMAÇÃO DESEJA PREENCHER? ")
                    sleep(2)
                    print("Alterado com sucesso!")

                elif i == 3:  # Excluir usuário

                    for x in range(0, len(listaUsuario)):
                        print(f"{x + 1} - {listaUsuario[x][0]}")
                    i = int(input("QUAL USUÁRIO DESEJA EXCLUIR? "))

                    del listaUsuario[i - 1]
                    print("Usuário removido do sistema.")
                    sleep(2)

            elif i ==2:  # Menu de ações para realizar com os dados das empresas.
                print("Opção 2 ok")

            elif i == 0:  # Saida
                print("Volte sempre!")

            else:
                print("Digite uma opção valida!")

        except ValueError:
            print("\nInsira uma opção valida.")

        finally:
            sleep(1)
            print("\nOperação finalizada")



































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
                print(f"""A simulação com a empresa {nomeEmpresa} foi concluída!
Iremos te retornar para o menu inicial em alguns segundos...""")
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
1 - Ponto principal 1
2 - Ponto principal 2
3 - Ponto principal 3
4 - Ponto principal 4
5 - Ponto principal 5 

Para leitura completa do tópico selecione um item, ou: 

99 - VOLTAR AO MENU INICIAL
0 - SAIR

DIGITE UMA OPÇÃO: """))

                if 1 <= i <= 5:
                    # Apresentação completa do ponto escolhido pelo usuário
                    print(f"DESCRIÇÃO COMPLETA DO TOPICO {i}")
                    print("Ação 2 finalizada, em alguns segundos iremos te retornar para o menu principal...")
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
                    print(f"\nTexto sobre a informação {i}...")
                    print("Ação 3 finalizada, em alguns segundos iremos te retornar para o menu principal...")
                    sleep(7)
                    i = 99

        elif i == 0:
            # Finalização da utilização do sistema
            print("Volte sempre!")

        else:
            # Tratativa de erro caso o usuário selecionar uma opção não existente
            print("Digite uma opção válida! ")
            sleep(1)
            i = 99
