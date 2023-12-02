# Crie um programa que leia vários números inteiros pelo teclado.
# O programa vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles deconsiderando o flag
numeros = cont = soma = 0
while numeros != 999:
    numeros = int(input('Digite um valor: '))
    cont += 1
    soma += numeros

print(f'Foram digitados {cont - 1} números')
print(f'E sua soma é: {soma - 999}')
