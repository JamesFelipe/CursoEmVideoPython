# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = input('Digite seu nome: ').strip().lower()
print(f'A pessoa tem "Silva" no nome? {"silva" in nome}')
