# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos.
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

nTotal = int(input('Insira o número total de eleitores: '))
nBranco = int(input('Insira o número de votos branco: '))
nNulos = int(input('Insira o número de votos nulos: '))
nValidos = int(input('Insira o número de votos válidos: '))

porBranco = int(nBranco*100)/nTotal
porNulos = int(nNulos*100)/nTotal
porValido = int(nValidos*100)/nTotal

print(f''' O percentual de votos referente a {nTotal} é:
Votos brancos = {porBranco:.2f}%
Votos nulos = {porNulos:.2f}%
Votos válidos = {porValido:.2f}% ''')