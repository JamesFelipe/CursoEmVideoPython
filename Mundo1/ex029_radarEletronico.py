# Escreva um programa que leia a velocidade de um carro

# Se ele utrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada Km acima do limite

velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado e vai pagar: {multa:.2f}R$')
else:
    print('Tudo dentro dos conformes, Tenha uma boa noite')
