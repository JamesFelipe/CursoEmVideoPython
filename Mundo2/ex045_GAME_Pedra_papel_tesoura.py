# Crie um programa que faça o computador jogar Jokenpô com você
from random import choice
from time import sleep

computador = ['pedra', 'papel', 'tesoura']
aleatorio = choice(computador)
jogador = input('Digite sua jogada: ')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print()

if aleatorio == jogador:
    print(f'Computador jogou {aleatorio}')
    print(f'Jogador jogou {jogador}')
    print('EMPATE claro')
elif jogador == 'pedra' and aleatorio == 'tesoura' \
    or jogador == 'papel' and aleatorio == 'pedra' \
    or jogador == 'tesoura' and aleatorio == 'papel':
    print(f'Computador jogou: {aleatorio}')
    print(f'Jogador jogou: {jogador}')
    print('Parabéns, você venceu! \U0001F3C6')
else:
    print(f'Computador jogou: {aleatorio}')
    print(f'Jogador jogou: {jogador}')
    print('Que pena, você perdeu! \U0001FAE0')
