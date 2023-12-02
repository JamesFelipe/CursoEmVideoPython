# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma sequência de Fibonacci
# Ex.: 0 -> 1 -> 2 -> 3 -> 5 -> 8
print('_' * 30)
print('Sequência de Fibonnaci')
print('_' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')
for valor in range(1, n - 1):
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
print(' -> FIM')
