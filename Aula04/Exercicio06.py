# Considerando a idade de uma pessoa, exiba se ela pode doar sangue (idade entre
# 18 e 67 anos) ou não (idade menor que 18 anos ou maior que 67 anos).

idade = int(input('Digite sua idade para saber se pode doar sangue: '))

if 18 <= idade <=67:
    print(f'Sua idade é {idade}, você pode doar sangue.')

else:
    print(f'A sua idade é {idade}, você não pode doar sangue. ')
