"""Faça um programa que verifique se uma "senha" de dois dígitos (um número entre 0 e 99, inclusive) digitada pelo
usuário está correta. O programa deve repetir o pedido até que o usuário escreva o valor correto. A senha correta
deve estar definida no próprio programa. """

senhaUsuario = int(input("Digite a senha: "))
senhaCorreta = int(25)

while senhaUsuario != senhaCorreta:
    print("Senha invalida!")
    senhaUsuario = int(input("Digite a senha: "))

print("Acesso liberado.")