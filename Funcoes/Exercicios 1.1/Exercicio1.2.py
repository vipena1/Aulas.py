"""
Autor: Vinicius Pena
Programa: Exercicio Python
Aula: Função
Data: 23/02/2023
Utilizando o conceito do número indeterminado de argumentos chave, crie uma função que imprima o nome,
 sobrenome e
idade de uma pessoa desde que ela tenha mais de 20 anos. #dica use chaves pnome, psobrenome, pidade. OBS: o programa
deve ter, obrigatoriamente, a função “main” """

def main():
    # Criando Dicionario
    pessoa1 = {'pnome': 'João', 'psobrenome': 'Silva', 'pidade': 18}
    pessoa2 = {'pnome': 'Maria', 'psobrenome': 'Souza', 'pidade': 25}
    pessoa3 = {'pnome': 'José', 'psobrenome': 'Fernandes', 'pidade': 30}

    imprimir_pessoa(**pessoa1)  # não imprime nada, idade < 20
    imprimir_pessoa(**pessoa2)  # imprime "Maria Souza 25"
    imprimir_pessoa(**pessoa3)  # imprime "José Fernandes 30"


def imprimir_pessoa(**pessoa):  # Com ** ele trabalha com dicionario, com * ele trabalha com lista
    if pessoa.get('pidade') > 20:
        print(pessoa.get('pnome'), pessoa.get('psobrenome'), pessoa.get('pidade'))

if (__name__ == '__main__'):
    main()
