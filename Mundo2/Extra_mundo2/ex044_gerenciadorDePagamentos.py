# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e conição de pagamento:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# em até 2x no cartão preço normal
# 3x ou mais no cartão 20% de juros

produto = float(input('Digite o preço do produto R$: '))
opcao = int(input('''Escolha como você quer pagar: 
1 - À vista dinheiro/cheque: 10% de desconto
2 - À vista no cartão: 5% de desconto
3-  em até 2x no cartão preço normal
4-  3x ou mais no cartão 20% de juros
Sua opção[Número]: '''))

match opcao:
    case 1:
        desconto = produto - (produto * 10/100)
        print(f'Com desconto de 10% você vai pagar: {desconto:.2f}R$')
    case 2:
        desconto = produto - (produto * 5 / 100)
        print(f'Com desconto de 5% você vai pagar: {desconto:.2f}R$')
    case 3:
        parcelas = produto / 2
        print(f'Você irá pagar o produto em 2 parcelas de {parcelas:.2f}R$')
    case 4:
        juros = produto + (produto * 20/100)
        print(f'No final(com 20% de juros) você irá pagar {juros:.2f}R$')
    case invalido:
        print('Valor inválido')
