""" - Desenvolvimento em Python de um menu listando todas as funcionalidade do sistema;
- Ao escolher uma opção, o programa deverá mostrar na tela a opção selecionada e os sub-menus da opção selecionada;
- Quando um menu não tiver mais sub-menus, retornar na tela de menu principal;
- Criar um menu sair, que encerra o programa."""

from time import sleep

i = 99

while i != 0:

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
