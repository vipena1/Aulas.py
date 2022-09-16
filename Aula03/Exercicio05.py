# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias.
# Considerar ano com 365 dias e mês com 30 dias

import datetime

data = str(input('Insira a data de nascimento: '))
dataatual = datetime.datetime.today()

dia = int(data[slice(0, 2)])
mes = int(data[slice(3, 5)])
ano = int(data[slice(6, 10)])

if dataatual.month < mes and dataatual.day < dia:
    ano = dataatual.year - ano - 1
    mes = mes - dataatual.month
    dia = dia - dataatual.day

elif dataatual.month < mes and dataatual.day >= dia:
    ano = dataatual.year - ano - 1
    mes = mes - dataatual.month
    dia = dataatual.day - dia

elif dataatual.month > mes and dataatual.day < dia:
    ano = dataatual.year - ano
    mes = dataatual.month - mes
    dia = dia - dataatual.day

elif dataatual.month > mes and dataatual.day >= dia:
    ano = dataatual.year - ano
    mes = dataatual.month - mes
    dia = dataatual.day - dia

diasAno = ano*365
mesAno = mes*30
totalDias = mesAno+diasAno+dia

print(totalDias)
