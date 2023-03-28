listaCod = []
listaNome = []
listaSenha = []

resp = "S"

while resp != "N":
    print("1 - Inserir usuario")
    print("2 - Exibir dados do usuario")
    opc = int(input("Digite a opção: "))

    if opc == 1:
        try:
            cod = int(input("Digite o codigo do usuario: "))
            nome = str(input("Digite o nome do usurio: "))
            senha = str(input("Digite a senha do usuario: "))

        except ValueError:
            print("Digite um valor numerico no codigo")

        else:
            listaCod.append(cod)
            listaNome.append(nome)
            listaSenha.append(senha)

        finally:
            print("Operação finalizada")

    elif opc == 2:
        print(listaCod)
        print(listaNome)
        print(listaSenha)

    resp = input("Deseja continuar? ( S / N ): ")


