# José Carlos da Silva
# 97385
# Vinicius de Abreu Pena
# 96881

def calcular_ipva(**carro):
    if carro['tempo_fabricacao'] < 20:
        imposto = carro['valor'] * 0.04
    else:
        imposto = 0
    return imposto


def main():
    carros = [
        {'nome': input("nome: "), 'marca': input("marca: "), 'quilometragem': input("km: "), 'tempo_fabricacao': int(input("idade: ")), 'valor': float(input("preço: "))},
        {'nome': input("nome: "), 'marca': input("marca: "), 'quilometragem': input("km: "), 'tempo_fabricacao': int(input("idade: ")), 'valor': float(input("preço: "))},
        {'nome': input("nome: "), 'marca': input("marca: "), 'quilometragem': input("km: "), 'tempo_fabricacao': int(input("idade: ")), 'valor': float(input("preço: "))},
        {'nome': input("nome: "), 'marca': input("marca: "), 'quilometragem': input("km: "), 'tempo_fabricacao': int(input("idade: ")), 'valor': float(input("preço: "))},
        {'nome': input("nome: "), 'marca': input("marca: "), 'quilometragem': input("km: "), 'tempo_fabricacao': int(input("idade: ")), 'valor': float(input("preço: "))}
    ]

    for carro in carros:
        imposto = calcular_ipva(**carro)
        print(f"O imposto de IPVA do carro {carro['nome']} é de R$ {imposto:.2f}")


if __name__ == '__main__':
    main()
