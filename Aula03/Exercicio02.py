# Tendo como base o valor da cotação do dólar (em reais) do dia, faça a conversão de um valor em dólares para reais.

dolar = float(input('Insira a quantidade de dolar para converter em real: $'))
cotacao = float(input('Insira a cotação do dolar a ser calculado: $'))

real = dolar*cotacao

print(f'A conversão para real é: R${real:.2f}')