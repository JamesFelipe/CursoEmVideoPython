# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = input('Digite o nome da sua cidade: ').strip().lower()
print('A cidade começa com "SANTO"? ', cidade[0:5] == 'santo')
