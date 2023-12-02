# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o
soma = 0
for i in range(0, 6):
    n = int(input(f'Digite o {i+1}º número inteiro: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares é {soma}')
