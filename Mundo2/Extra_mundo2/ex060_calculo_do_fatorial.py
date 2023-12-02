# Faça um programa que leia um número qualquer e mostre o seu fatorial
# ex.: 5! = 5 x 4 x 3 x 2 x 1
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1

for valor in range(c):
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1  
print(f'{f}')