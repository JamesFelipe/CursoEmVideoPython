# Faça um programa que leia o peso de cinco pessoas. no final mostre qual foi o maior e o menor peso lidos
maior = menor = 0
for i in range(1, 6):
    pesos = float(input(f'Digite o peso da {i}ª pessoa: '))
    if i == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos > maior:
            maior = pesos
        if pesos < menor:
            menor = pesos

print(f'O maior peso é {maior}')
print(f'O menor peso é {menor}')
