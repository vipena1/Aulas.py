# Crie um algoritmo que solicite ao usuário seu consumo de energia elétrica (em kWh), que deve ser uma variável real.
# O algoritmo deve, então, calcular o total da conta, considerando que cada kWh custa R$ 0,20.

consumo = float(input('Insira o consumo de energia em kWh para o calculo: '))

calculo = consumo*0.20

print(f'O valor da conta ficou R${calculo:.2f}')


