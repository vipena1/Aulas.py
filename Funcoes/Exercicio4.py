# uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.

data = input("Digite sua data de nascimento (DD/MM/AAAA): ")


def dataEscrita(data):
    listaData = data.split("/")

    listaMes = ["janeiro", "fevereiro", "março",
                "abril", "maio", "junho",
                "julho", "agosto", "setembro",
                "outubro", "novembro", "dezembro"]

    mesEscrito = listaMes[int(listaData[1]) - 1]

    return f"{listaData[0]} de {mesEscrito} de {listaData[2]}"


print(dataEscrita(data))
