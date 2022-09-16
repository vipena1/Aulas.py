"""Mostrar todos os inteiros entre dois números digitados pelo usuário. Exemplo: usuário digita os números 8 e 15,
e aparecem em tela: 9, 10, 11, 12, 13, 14. """

numUm = int(input("Digite o primeiro número onde deseja iniciar os números a serem mostrados: "))
numDois = int(input("Digite o segundo número onde deseja para os números a serem mostrados: "))

cont = numUm + 1
while cont < numDois:
    print(cont)
    cont = cont + 1
