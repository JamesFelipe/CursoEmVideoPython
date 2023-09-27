# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date

ano = int(input('Digite o ano: 0 para pegar o ano atual: '))
if ano == 0:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é BISSEXTO')
else:
    print(f'{ano} Não é Bissexto')
