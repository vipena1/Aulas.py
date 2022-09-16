# Dada a quilometragem parcial de um carro e a quantidade de litros gastos ele para percorrer esta quilometragem,
# fazer um algoritmo que calcule quantos Km/l o carro percorreu.

km = float(input('Insira a quilometragem percorrida para calculo: '))
litros = float(input('Insira a litragem consumida: '))

calculo = km/litros

print(f'O consumo do veiculo no percurso de {km}, foi de {calculo:.2f}Km/L')