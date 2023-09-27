# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado
km = float(input('Quantos quilometros você percorreu? ')) * 0.15
dias = int(input('Por quantos dias o carro foi alugado? ')) * 60
total = km + dias
print(f'Você terá que pagar {total:.2f}R$')
