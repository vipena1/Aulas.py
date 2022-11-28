from time import sleep

login = 1111111111
listaRecompensas = []
totalPontos = 0

while login != 0:

    # Menu principal
    if login == 1111111111:  # Só aparecera a mensagem de login realizado no primeiro acesso
        login = int(input("""\nLogin realizado com sucesso.
Digite a opção desejada:
1 - Transporte sustentavel/SMART
2 - Pontos de recarga
3 - Minhas recompensas
4 - Como conseguir recompensas
0 - Sair

QUAL OPÇÃO DESEJA SELECIONAR? """))

    # Menu principal caso o usuário queira retornar para ele
    if login == 99:
        login = int(input("""\nDigite a opção desejada:
1 - Transporte sustentavel/SMART
2 - Pontos de recarga
3 - Minhas recompensas
4 - Como conseguir recompensas
0 - Sair

QUAL OPÇÃO DESEJA SELECIONAR?"""))

    # Opção 1 do menu incial dara a opção de selecionar qual o meio de tranporte o usuário vai usar
    if login == 1:
        login = int(input("""\nSelecione o meio de transporte sustentavel/SMART:
1 - Patinete
2 - Bicicleta
3 - Moto elétrica
4 - Carro elétrico
99 - Voltar para o menu inicial
0 - Sair

QUAL OPÇÃO DESEJA SELECIONAR? """))

        # Opção 1 do menu 1 é quando o usuário ira usar um patinete, o sistema vai calcular os pontos de acordo com os KM andados
        if login == 1:
            login = int(input("""\nVocê selecionou PATINETE!
Digite a quantidade de quilometros que ira percorrer, 99 para voltar ao inicio ou 0 para sair: """))

            if login == 99 or login == 0:
                login = login
            else:
                pontosPatinete = login * 10
                totalPontos = totalPontos + pontosPatinete
                textoPatinete = f"Patinete, {pontosPatinete} pontos"
                listaRecompensas.append(textoPatinete)
                print("Salvando dados...")
                sleep(2)
                login = 99

        # Opção 2 do menu 1 é quando o usuário ira usar uma bicicleta, o sistema vai calcular os pontos de acordo com os KM andados
        elif login == 2:
            login = int(input("""\nVocê selecionou BICICLETA!
Digite a quantidade de quilometros que ira percorrer, 99 para voltar ao inicio ou 0 para sair: """))

            if login == 99 or login == 0:
                login = login

            else:
                pontosBicicleta = login * 8
                totalPontos = totalPontos + pontosBicicleta
                textoBicicleta = f"Patinete, {pontosBicicleta} pontos"
                listaRecompensas.append(textoBicicleta)
                print("Salvando dados...")
                sleep(2)
                login = 99

