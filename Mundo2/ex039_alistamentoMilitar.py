# Faça um programa que leia o ano de nascimento de uma pessoa e informe de acordo com sua idade

# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se já passou do tempo de alistamento

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date

nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade < 18:
    anos_que_faltam = 18 - idade
    print(f'Faltam {anos_que_faltam} anos para você se alistar no exército')
elif idade == 18:
    print('Está na hora de se alistar no exército')
elif idade > 18:
    anos_que_faltam = idade - 18
    print(f'Você já deveria ter se alistado há {anos_que_faltam} anos')
