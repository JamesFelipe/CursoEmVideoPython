# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
numeros = soma = cont = 0
maior = menor = 0
opcao = 's'
while opcao == 's':
    numeros = int(input('Digite um valor: '))
    cont += 1
    soma += numeros
    if cont == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    opcao = input('Você quer adicionar mais valores: s/n ')

print(f'A média dos valores é {soma / cont:.2f}')
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')
