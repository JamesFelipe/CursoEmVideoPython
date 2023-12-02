# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a seguinte mensagem:

# O primeiro valor é maior
# o segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('o segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
