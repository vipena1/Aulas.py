# Considerando o IMC (índice de massa corpórea), calculado como peso/(altura*altura),
# exiba a situação da pessoa com base na seguinte tabela:

# IMC / Situação
# <= 18.5 / Abaixo do peso
# >18.5 e <=24.9 / Peso ideal
# >24.9 / Acima do peso

peso = float(input('Insira o peso para o calculo: '))
altura = float(input('Insira a altura para calculo: '))

imc = peso/ altura**2

if imc <= 18.5:
    print('Você está abaixo do peso. ')

elif 18.5 < imc <= 24.9:
    print('Você está no peso ideal.')

elif imc > 24.9:
    print('Você está acima do peso.')

else:
    print('ERRO')