# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# considere US$ 1,00 = 3,27
real = float(input('Digite quanto dinheiro você tem na carteira: '))
dolar = real / 3.27
print(f'Com {real}R$ você pode comprar {dolar:.2f}US$')
