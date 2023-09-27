# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas
km = float(input('Digite a distância da viagem em quilometros: Km '))
if km <= 200:
    custo = km * 0.50
    print(f'Com {km}Km percorridos você pagará {custo:.2f}R$')
else:
    custo = km * 0.45
    print(f'Com {km}Km percorridos você pagará {custo:.2f}')
