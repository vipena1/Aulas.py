# Uma livraria resolveu fazer uma promoção, com os seguintes critérios:
# - Livros com preços até R$ 10,00 - desconto de 8%
# - Livros com preços de R$ 10,01 até R$ 60,00 - desconto de 10%
# - Livros com preços acima de R$ 60,00 - desconto de 20%
# Escreva um algoritmo que leia o preço do livro e mostre o valor do desconto oferecido, em reais.

preco = float(input('Insira o valor do livro que deseja comprar: R$'))

if 0 < preco <= 10:
    print(f'O livro tera um desconto de 8%, ficando com o valor de R${preco - (preco*0.08) :.2f}')

elif 10 < preco <= 60:
    print(f'O livro tera um desconto de 10%, ficando com o valor de R${preco - (preco * 0.1) :.2f}')

elif preco > 60:
    print(f'O livro tera um desconto de 20%, ficando com o valor de R${preco - (preco*0.2) :.2f}')

else:
    print('ERRO')