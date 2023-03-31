''''
resposta = input("Diga um numero :")
while resposta.isnumeric() == False:
    resposta = input("É numero que vc tem que digitar poxa : ")
resposta = int(resposta)
print("acertou")
'''
'''
resposta = input("Cadastre uma senha : ")
num_tentativas = 1
while len(resposta)!= 6 and num_tentativas < 3:
    num_tentativas +=1
    print(f"foram {len(resposta)} digitos, tolinho é 6")
    print(f"faltam {3-num_tentativas} tentativas")
    resposta = input("Cadastre uma senha : ")

if num_tentativas <3:
    print("parabéns vc acertou!")
else:
    print("vc errou")
'''
resposta = input("Gostaria de comprar algum produto?")
if resposta == "sim" :
    print()

amaciante = int("20")
sabão = int("12")
detergente = int("5")
print("Qual produto voce gostaria de comprar? ")
print("Digite 1 para amaciante")
print("Digite 2 para sabão")
print("Digite 3 para detergente")

resposta = input("Escolha uma opção:")



