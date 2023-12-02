# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e conição de pagamento:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# em até 2x no cartão preço normal
# 3x ou mais no cartão 20% de juros

produto = float(input('Digite o preço do produto: '))
opcao = int(input('''
Escolha como vai pagar:
[ 1 ] - À vista no dinheiro/cheque com 10% de desconto
[ 2 ] - À vista no cartão com 5% de desconto
[ 3 ] - Em até 2x no cartão(preço normal)
[ 4 ] - 3x ou mais no cartão com 20% de juros

Escolha: '''))

if opcao == 1:
    desconto = produto - (produto * 10/100)
    print(f'Antes o produto custava {produto}R$ com 10% de desconto vai custar: {desconto:.2f}R$')
elif opcao == 2:
    desconto = produto - (produto * 5/100)
    print(f'Antes o produto custava {produto}R$ com 5% de desconto vai custar: {desconto:.2f}R$')
elif opcao == 3:
    parcelas = produto / 2
    print(f'Antes o produto custava {produto}R$ você vai pagar {parcelas:.2f}R$ 2 vezes')
elif opcao == 4:
    juros = produto + (produto * 20/100)
    print(f'Antes o produto custava {produto}R$ com 20% de aumentoo vai custar: {juros:.2f}R$')
else:
    print('Opção inválida')
