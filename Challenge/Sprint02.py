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
4 - COMPONENTES
0 - SAIR
    
QUAL OPÇÃO DESEJA SELECIONAR? """))

    if i == 1:
        # Função ao executar a opção 1 do menu principal
        print("""ESSE É O NOSSO SIMULADOR DE INVESTIMENTOS, PARA UTILIZA-LO, PREENCHA OS CAMPOS ABAIXO:""")
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
        # Função ao executar a opção 1 do menu principal
        print("\nSELECIONE UM DOCUMENTO DA LISTA SUSPENSA")
        i = int(input("""1 - DOCUMENTO 1
2 - DOCUMENTO 2
3 - DOCUMENTO 3
4 - DOCUMENTO 4
99 - VOLTAR AO MENU INICIAL
0 - SAIR

DIGITE UMA OPÇÃO: """))

        if i != 99 and i != 0:
            i = int(input(f"""\nOs principais pontos do documento {i} são:
1 - Ponto principal 1
2 - Ponto principal 2
3 - Ponto principal 3
4 - Ponto principal 4
5 - Ponto principal 5 

Para leitura completa do topico selecione um item, ou: 

99 - VOLTAR AO MENU INICIAL
0 - SAIR

DIGITE UM OPÇÃO: """))

            if i != 99 and i != 0:
                print(f"""DESCRIÇÃO COMPLETA DO TOPICO {i}""")
                print("Ação 2 finalizada, em alguns segunso iremos te retornar para o menu principal...")
                sleep(7)
                i = 99

    elif i == 0:
        # Finalização da utilização do sistema
        print("Volte sempre!")

    else:
        print("Digite um opção valida! ")
        sleep(3)
        i = 99