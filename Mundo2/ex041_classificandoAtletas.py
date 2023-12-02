# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima master
from datetime import date

ano_atual = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = ano_atual - nascimento
if idade <= 9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta Infantil')
elif idade <= 20:
    print('Atleta SÊNIOR')
elif idade > 20:
    print('Atleta MASTER')
