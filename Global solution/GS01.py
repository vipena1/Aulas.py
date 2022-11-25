from time import sleep

login = 99
listaRecompensas = []

while login != 0:
    login = int(input("""Login realizado com sucesso.
Digite a opção desejada:
1 - Transporte sustentavel/SMART
2 - Pontos de recarga
3 - Minhas recompensas
4 - Como conseguir recompensas
0 - Sair"""))
