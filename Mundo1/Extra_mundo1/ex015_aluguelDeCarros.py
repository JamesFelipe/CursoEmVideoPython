# Resolvendo mais uma vez
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado
km = float(input('Digite a quantidade de quilometros percorridos: Km ')) * 0.15
dias = int(input('Digite a quantidade de dias pelo qual o carro foi alugado: ')) * 60
total = km + dias
print(f'No final da sua viagem você irá pagar {total:.2f}R$')
