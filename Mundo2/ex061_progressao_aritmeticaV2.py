# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# na progressão usando a estrutura while
termo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da PA são> ', end='')

i = 0
while i < 10:
    a_n = termo + (i) * razao
    i += 1
    print(a_n, end=', ')
print('fim')
