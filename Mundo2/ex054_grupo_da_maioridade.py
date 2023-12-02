# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade a quantas já são maiores
from datetime import date
atual = date.today().year
cont_maior = cont_menor = 0

for i in range(0, 7):
    nascimento = int(input(f'Digite a data de nascimento da {i+1}ª pessoa: '))
    idade = atual - nascimento
    if idade >= 18:
        cont_maior += 1
    elif idade < 18:
        cont_menor += 1
print(f'{cont_maior} pessoas já atigiram a maior idade')
print(f'{cont_menor} pessoas ainda são de menor')
