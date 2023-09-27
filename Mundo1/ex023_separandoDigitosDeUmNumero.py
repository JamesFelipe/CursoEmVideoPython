# Faça um programa que leia um número de 0 a 9999 e mostre na tela cadaum dos dígitos separados
# Ex: Digite um número: 1834

# Unidade: 4
# dezena: 3
# centena: 8
# milhr: 1

# String
n = input('Digite um valor de 0 a 9999: ')
print(f'unidade: {n[3]}')
print(f'dezena: {n[2]}')
print(f'centena: {n[1]}')
print(f'milhar: {n[0]}')

print()
# matemática
n = int(input('Digite um valor inteiro de 0 a 9999: '))

unidade = n % 10
dezena = n % 100 // 10
centena = n % 1_000 // 100
milhar = n% 10_000 // 1000
print('Unidade: ', unidade)
print('Dezena: ', dezena)
print('Centena: ', centena)
print('Milhar', milhar)

