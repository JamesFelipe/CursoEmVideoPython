# Escreva um programa para aprovar um empréstimo para a compra de uma casa
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar

# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite quanto você ganha: '))
anos = int(input('Digite em quantos anos você vai pagar: '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de {casa:.2f}R$ em {anos} anos\
  a prestação será de {prestacao:.2f}R$')

if prestacao <= minimo:
    print('Empréstimo concedido')
else:
    print('Empréstimo negado') 
