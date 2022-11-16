""" - Desenvolvimento em Python de um menu listando todas as funcionalidade do sistema;
- Ao escolher uma opção, o programa deverá mostrar na tela a opção selecionada e os sub-menus da opção selecionada;
- Quando um menu não tiver mais sub-menus, retornar na tela de menu principal;
- Criar um menu sair, que encerra o programa."""

from time import sleep

i = 99

while i != 0:

    if i == 99:
        i = int(input("""\nBEM-VINDO!
PARA NAVEGAR ENTRE OS MENUS, DIGITE O NÚMERO DESEJADO:
1 - SIMULADOR
2 - DOCUMENTAÇÃO
3 - INFORMAÇÕES
4 - COMPONENTES
0 - SAIR
    
QUAL OPÇÃO DESEJA SELECIONAR? """))

    if i == 1:
        print("""ESSE É O NOSSO SIMULADOR DE INVESTIMENTOS, PARA UTILIZA-LO, PREENCHA OS CAMPOS ABAIXO:""")
        nomeEmpresa = str(input("Digite o nome da empresa: "))
        setorEmpresa = str(input("Digite o setor atuante da empresa: "))
        anoAbertura = int(input("Digite o ano de abertura: "))
        i = int(input("DIGITE 1 PARA CONTINUAR, 99 PARA VOLTAR AO INICIO OU 0 PARA SAIR: "))

        if i == 1:
            print("REALIZANDO SIMULAÇÃO...")
            sleep(2)
            print(f"""A simulação com a empresa {nomeEmpresa} foi concluida!
Iremos te retornar para o menu inicial em alguns segundos...""")
            sleep(5)
            i = 99

    if i == 0:
        print("Volte sempre!")
        sleep(2)
