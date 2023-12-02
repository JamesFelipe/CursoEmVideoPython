# Melhore o desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
# para vencer
from random import randint

aleatorio = randint(0, 10)
numero = cont = 0
while numero != aleatorio:
    numero = int(input('Digite qual número você acha que eu pensei: '))
    cont += 1

    if numero == aleatorio:
        print(f'Parabéns, realmente pensei no {numero} \U0001f947')
        print(f'Você acertou com {cont} tentativas')
    elif numero > aleatorio:
        print('Pensei em um número menor...')
    elif numero < aleatorio:
        print('Pensei em um número maior')
