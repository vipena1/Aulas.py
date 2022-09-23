# Simulação "FOR"

for cont in range(1, 4):
    n1 = float(input(f"Entre com a primeira nota do aluno {cont}: "))
    n2 = float(input(f"Entre com a segunda nota do aluno {cont}: "))
    n3 = float(input(f"Entre com a terceira nota do aluno {cont}: "))

    media = (n1+n2+n3)/3

    print(f"Média do aluno {cont} = {media:.2f}")