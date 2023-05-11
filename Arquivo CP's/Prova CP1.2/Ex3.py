# José Carlos da Silva
# 97385
# Vinicius de Abreu Pena
# 96881

resultados = []

for i in range(5):
    palavra = input("Digite a palavra " + str(i+1) + ": ")
    resultados.append(palavra)

palindromo = list(map(lambda x: 1 if x == x[::-1] else 0, resultados))

print(palindromo)
