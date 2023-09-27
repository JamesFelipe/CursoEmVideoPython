# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ')
print(f'O nome em maiúsculo é: {nome.upper()}')
print(f'O nome em minúsculo é: {nome.lower()}')

# Separando o nome em listas
separador = nome.split()
# Unindo as listas
uniao = ''.join(separador)
print(f'Sem contar espaços o seu nome tem {len(uniao)} caracteres')

separador2 = nome.split()[0].strip()
print(f'O seu primeiro nome tem {len(separador2)} caracteres')

