# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final mostre os 10 primeiros termos dessa 
termo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da PA são> ', end='')
for i in range(0, 10):
    a_n = termo + (i) * razao
    print(a_n, end=', ')
print('Fim') 
