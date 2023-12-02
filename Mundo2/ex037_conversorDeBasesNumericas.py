# Escreva um programa que leia um número inteiro qualquer e peçapara o usuário escolher qual será a base de conversão:

# 1 - para binário
# 2 - para octal
# 3 - para hexadecimal

n = int(input('Digite um valor inteiro: '))
opcao = int(input('''
Digite para qual valor você quer converter:
[ 1 ] - Binário
[ 2 ] - Octal
[ 3 ] - Hexadecimal

opcao: '''))

if opcao == 1:
    print(f'{n} em binário é {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} em octal é {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} em hexadecimal é "{hex(n)[2:]}"')
