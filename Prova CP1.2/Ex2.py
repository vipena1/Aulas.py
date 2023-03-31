# José Carlos da Silva
# 97385
# Vinicius de Abreu Pena
# 96881

aplica_bonus = lambda salario, vendas: salario * 1.1 if vendas <= 5000 else salario * 1.2

salarios = []

for i in range(10):
    salario = float(input("Digite o salário do funcionário {}: ".format(i+1)))
    vendas = float(input("Digite o total de vendas do funcionário {} nos últimos 3 meses: ".format(i+1)))
    salario_com_bonus = aplica_bonus(salario, vendas)
    salarios.append(salario_com_bonus)

print("Lista de salários com bônus:")
print(salarios)

