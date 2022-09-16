# Considerando o salário de um funcionário, dê um acréscimo de 10% se o valor for
# maior ou igual a 800,00; caso contrário, o acréscimo será de 20%

salario = float(input('Insira o sálario que recebera o acréscimo: R$'))

if salario >= 800:
    salario = (salario*0.10)+salario

else:
    salario = (salario*0.20)+salario

print(f'O sálario informado com acréscimo ficoi igual a : R${salario}.')
