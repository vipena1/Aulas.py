try:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    div = num1 / num2

except ValueError:
    print("Digite um valor numerico")

except ZeroDivisionError:
    print("Insira um valor diferente de 0")

else:
    print(f"A divisão dos dois numeros é: {div:.2f}")

finally:
    print("Operação finalizada")