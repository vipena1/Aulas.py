qtdHabitantes = 0
somaSalario = 0
somaFilhos = 0
maiorSalario = 0
salarioMenor150 = 0

salario = float(input("Digite o salario:"))

while salario >= 0:
    numFilho = int(input("Digite o número de filhos: "))

    somaSalario = somaSalario + salario
    somaFilhos = somaFilhos + numFilho

    if salario > maiorSalario:
        maiorSalario = salario

    if salario < 150:
        salarioMenor150 = salarioMenor150 + 1

    qtdHabitantes = qtdHabitantes + 1

    salario = float(input("Digite o salario: "))

percMenor150 = (salarioMenor150 * 100) / qtdHabitantes
mediaSalario = somaSalario / qtdHabitantes
mediaFilhos = somaFilhos / qtdHabitantes

print(f"A média de salario da população é: R${mediaSalario}")
print(f"A média de número de filhos é: {mediaFilhos}")
print(f"O maior salário é: R${maiorSalario}")
print(f"O percentual de pessoas com salário menor que R$150 é: {percMenor150}")