# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado peça  a digitação novamente até ter um valor correto
sexo = ''
while sexo != 'm' and sexo != 'f':
    sexo = input('Digite seu sexo: M/F ').strip().lower()
    if sexo == 'm' or sexo == 'f':
        print(f'Valor {sexo.upper()} registado com sucesso')
    else:
        print('Dados inválidos')

