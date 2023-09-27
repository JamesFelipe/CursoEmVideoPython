# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

aleatorio = randint(0, 5)
numero = int(input('Digite qual número você acha que eu pensei: '))

if numero == aleatorio:
    print(f'Parabéns, realmente pensei no {numero} \U0001f947')
else:
    print(f'Que pena, pensei no número: {aleatorio} \U0001F625')