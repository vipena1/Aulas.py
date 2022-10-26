""" Faça um programa em Python que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome
do mês por extenso. """

data = input("Digite sua data de nascimento (DD/MM/AAAA): ")

listaData = data.split("/")

listaMes = ["janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"]

textoMes = listaMes[int(listaData[1])-1]

print(listaData[0] + "/" + textoMes + "/" + listaData[2])


