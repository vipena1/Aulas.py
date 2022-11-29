from time import sleep

login = 1111111111
listaRecompensas = []
totalPontos = 0
x = 0

while login != 0:

    # Menu principal
    if login == 1111111111:  # Só aparecera a mensagem de login realizado no primeiro acesso
        login = int(input("""\nLogin realizado com sucesso.
Digite a opção desejada:
1 - Transporte sustentável/SMART
2 - Postos de veículos
3 - Minhas recompensas
4 - Como conseguir recompensas
0 - Sair

QUAL OPÇÃO DESEJA SELECIONAR? """))

    # Menu principal caso o usuário queira retornar para ele
    if login == 99:
        login = int(input("""\nDigite a opção desejada:
1 - Transporte sustentável/SMART
2 - Postos de veículos
3 - Minhas recompensas
4 - Como conseguir recompensas
0 - Sair

QUAL OPÇÃO DESEJA SELECIONAR? """))

    # Opção 1 do menu inicial dará a opção de selecionar qual o meio de transporte o usuário vai usar
    if login == 1:
        login = int(input("""\nSelecione o meio de transporte sustentável/SMART:
1 - Patinete
2 - Bicicleta
3 - Moto elétrica
4 - Carro elétrico
99 - Voltar para o menu inicial
0 - Sair

QUAL OPÇÃO DESEJA SELECIONAR? """))

        # Opção 1 do menu 1 é quando o usuário irá usar um patinete, o sistema vai calcular os pontos de acordo com os KM andados
        if login == 1:
            login = int(input("""\nVocê selecionou PATINETE!
Digite a quantidade de quilômetros que irá percorrer, 99 para voltar ao início ou 0 para sair: """))

            if login != 99 and login != 0:
                pontosPatinete = login * 10
                totalPontos = totalPontos + pontosPatinete
                textoPatinete = f"Patinete, {pontosPatinete} pontos"
                listaRecompensas.append(textoPatinete)
                x = x +1
                print("Salvando dados...")
                sleep(2)
                login = 99

        # Opção 2 do menu 1 é quando o usuário irá usar uma bicicleta, o sistema vai calcular os pontos de acordo com os KM andados
        elif login == 2:
            login = int(input("""\nVocê selecionou BICICLETA!
Digite a quantidade de quilômetros que irá percorrer, 99 para voltar ao início ou 0 para sair: """))

            if login != 99 and login != 0:
                pontosBicicleta = login * 8
                totalPontos = totalPontos + pontosBicicleta
                textoBicicleta = f"Bicicleta, {pontosBicicleta} pontos"
                listaRecompensas.append(textoBicicleta)
                x = x + 1
                print("Salvando dados...")
                sleep(2)
                login = 99

        # Opção 3 do menu 1 é quando o usuário irá usar uma moto elétrica, o sistema vai calcular os pontos de acordo com os KM andados
        elif login == 3:
            login = int(input("""\nVocê selecionou MOTO ELÉTRICA!
Digite a quantidade de quilômetros que irá percorrer, 99 para voltar ao início ou 0 para sair: """))

            if login != 99 and login != 0:
                pontosMoto = login * 6
                totalPontos = totalPontos + pontosMoto
                textoMoto = f"Moto elétrica, {pontosMoto} pontos"
                listaRecompensas.append(textoMoto)
                x = x + 1
                print("Salvando dados...")
                sleep(2)
                login = 99

        # Opção 4 do menu 1 é quando o usuário irá usar uma carro elétrico, o sistema vai calcular os pontos de acordo com os KM andados
        elif login == 4:
            login = int(input("""\nVocê selecionou CARRO ELÉTRICA!
Digite a quantidade de quilômetros que irá percorrer, 99 para voltar ao início ou 0 para sair: """))

            if login != 99 and login != 0:
                pontosCarro = login * 4
                totalPontos = totalPontos + pontosCarro
                textoCarro = f"Carro elétrica, {pontosCarro} pontos"
                listaRecompensas.append(textoCarro)
                x = x + 1
                print("Salvando dados...")
                sleep(2)
                login = 99

        # Opção 99 ou 0 para retornar ao menu inicial ou sair do sistema
        elif login == 99 or login == 0:
            login = login

        # Tratativa para erro caso o usuário selecione uma opção não valida
        else:
            print("Digite uma opção válida!")
            sleep(1)
            login = 99

    # Opção 2 do menu inicial, o usuário irá inserir o endereço em que ele quer buscar pontos de para retirar ou depositar o veículo
    elif login == 2:
        login = int(input("""\nEscolha qual o meio de transporte deseja buscar os postos: 
1 - Patinete
2 - Bicicleta
3 - Moto elétrica
4 - Carro elétrico
99 - Voltar para o menu inicial
0 - Sair

QUAL OPÇÃO DESEJA SELECIONAR? """))

        # Opção 1 do menu 2 é quando o usuário irá buscar por patinetes próximo ao endereço selecionado
        if login == 1:
            endereco = str(input("""\nVocê selecionou PATINETE!
Digite o endereço que deseja buscar nas proximidades por pontos para patinetes: 
Endereço: """))
            raioKm = float(input("Raio de distância em KM: "))
            print("\nBuscando endereços...")
            sleep(2)
            print(f"""\nAbaixo está a lista de endereços no raio de {raioKm}KM do endereço {endereco}:
LISTA DE ENDEREÇOS EXEMPLO...""")
            sleep(2)
            login = 99

        # Opção 2 do menu 2 é quando o usuário irá buscar por bicicletas próximo ao endereço selecionado
        elif login == 2:
            endereco = str(input("""\nVocê selecionou BICICLETA!
Digite o endereço que deseja buscar nas proximidades por pontos para bicicletas: 
Endereço: """))
            raioKm = float(input("Raio de distância em KM: "))
            print("\nBuscando endereços...")
            sleep(2)
            print(f"""\nAbaixo está a lista de endereços no raio de {raioKm}KM do endereço {endereco}:
LISTA DE ENDEREÇOS EXEMPLO...""")
            sleep(2)
            login = 99

        # Opção 3 do menu 2 é quando o usuário irá buscar por moto elétrica próximo ao endereço selecionado
        elif login == 3:
            endereco = str(input("""\nVocê selecionou MOTO ELÉTRICA!
Digite o endereço que deseja buscar nas proximidades por pontos para motos elétricas: 
Endereço: """))
            raioKm = float(input("Raio de distância em KM: "))
            print("\nBuscando endereços...")
            sleep(2)
            print(f"""\nAbaixo está a lista de endereços no raio de {raioKm}KM do endereço {endereco}:
LISTA DE ENDEREÇOS EXEMPLO...""")
            sleep(2)
            login = 99

        # Opção 4 do menu 2 é quando o usuário irá buscar por carros elétrico próximo ao endereço selecionado
        elif login == 4:
            endereco = str(input("""\nVocê selecionou CARRO ELÉTRICO!
Digite o endereço que deseja buscar nas proximidades por pontos para carros elétricos: 
Endereço: """))
            raioKm = float(input("Raio de distância em KM: "))
            print("\nBuscando endereços...")
            sleep(2)
            print(f"""\nAbaixo está a lista de endereços no raio de {raioKm}KM do endereço {endereco}:
LISTA DE ENDEREÇOS EXEMPLO...""")
            sleep(2)
            login = 99

        # Opção 99 ou 0 para retornar ao menu inicial ou sair do sistema
        elif login == 99 or login == 0:
            login = login

        # Tratativa para erro caso o usuário selecione uma opção não valida
        else:
            print("Digite um opção válida!")
            sleep(1)
            login = 99

    # Opção 3 do menu inicial, para a visualização da quantidade de pontos que o usuário tem acumulado
    elif login == 3:
        print("\nA baixo está a lista de suas recompensas: ")
        for i in range(0, x):
            print(listaRecompensas[i])

        print("\nEm alguns segundos iremos te retornar para o menu inicial...")
        sleep(5)
        login = 99

    # Opção 4 do menu inicial, para a visualização de como ganhar pontos
    elif login == 4:
        print("""Para você conseguir pontos para resgatar uma recompensa é simples, você precisa apenas utilizar um veículo sustentável/SMAR!
Para contabilizarmos os seus pontos, você precisa selecionar o veículo que está usando e quantos KM rodou.
Cada veículo recebe uma pontuação por KM andado, abaixo está a lista de quantos pontos por KM você recebera em cada veículo:

Patinetes: 10 pontos por quilometro rodado.
Bicicletas: 8 pontos por quilometro rodado.
Moto elétrica: 6 pontos por quilometro rodado.
Carro elétrico: 4 pontos por quilometro rodado.

Agora que já sabe quantos pontos vai receber, é só usar no site e juntar pontos para resgatar suas recompensas!""")
        sleep(8)
        login = 99

    # Opção 99 ou 0 para o usuário retornar ao menu ou sair do sistema
    elif login == 0 or login == 99:
        login = login

    # Tratativa para erro caso o usuário selecione uma opção não valida
    else:
        print("Selecione uma opção válida!")
        sleep(1)
        login = 99
