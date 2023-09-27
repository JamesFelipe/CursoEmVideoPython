# Faça um programa que leia três números e mostre qual é o maior e qual é o menor


# Esse código funciona até certo ponto
print('Digite alguns valores')
n1 = int(input('Primeiro valor:  '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

if n1 < n2 < n3:
    print(f'O menor valor digitado foi {n1}')
if n2 < n1 < n3:
    print(f'O menor valor digitado foi {n2}')
if n3 < n2 < n1:
    print(f'O menor valor digitado foi {n3}')
if n1 > n2 > n3:
    print(f'O maior valor digitado foi {n1}')
if n2 > n1 > n3:
    print(f'O maior valor digitado foi {n2}')
if n3 > n2 > n1:
    print(f'O maior valor digitado foi {n3}')


# Código do Curso em vídeo
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é maior
maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')


