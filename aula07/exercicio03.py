# Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B.
# A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que
# está em A passe para B e vice-versa. Ao final, escrever os valores que ficaram armazenados nas variáveis.

A = int(10)
B = int(20)

C = A
A = B
B = C

print(f'O valor de A é {A}, e o valor de B é {B}.')
