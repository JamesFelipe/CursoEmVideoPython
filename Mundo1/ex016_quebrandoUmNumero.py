# Crie um programa que leia o número real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex Digite o número: 6.127
# O número 6.127 tem a parte inteira 6

# Soluçõa 1
from math import trunc
n = float(input('Digite um valor com ponto flutuante: '))
print(f'a parte inteira de {n} é {trunc(n)}')

# Solução 2
print(f'a parte inteira de {n} é {int(n)}')
