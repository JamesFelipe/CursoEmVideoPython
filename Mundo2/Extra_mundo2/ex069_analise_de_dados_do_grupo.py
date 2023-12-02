# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar.
# no final mostre:

# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem mais de 20 anos


cont_18 = cont_homem = cont_mulher_20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo[Masculino/Feminino]: ').strip().lower()[0]
    continuar = input('Para continuar pressione qualquer tecla para sair digite a tecla n: ').strip().lower()[0]
    if idade > 18:
        cont_18 += 1
    if sexo == 'm':
        cont_homem += 1
    if sexo == 'f' and idade > 18:
        cont_mulher_20 += 1
    if continuar == 'n':
        break
print(f'Temos {cont_18} pessoas com mais de 18 anos')
print(f'{cont_homem} homens foram cadastrados')
print(f'Temos {cont_mulher_20} mulheres com mais de 20 anos')
