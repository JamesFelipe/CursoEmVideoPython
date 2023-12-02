# Escreva um programa que leia um número inteiro qualquer e peçapara o usuário escolher qual será a base de conversão:

# 1 - para binário
# 2 - para octal
# 3 - para hexadecimal
n = int(input('DIgite um valor para ser convertido: '))
opcao = int(input(''''Você quer converter para:
1 - Binário
2 - Octal
3 - Hexadecimal                
\n
Sua resposta [valor númerico]: '''))
match opcao:
    case 1:
        print(f'O valor {n} em binário é: {bin(n)[2:]}')
    case 2:
        print(f'O valor {n} em octal é: {oct(n)[2:]}')
    case 3:
        print(f'O valor {n} em Hexadecimal é: {hex(n)[2:]}')
    case outro:
        print('valor inválido')
