# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
produto = float(input('Digite o preço do produto: '))
desconto = produto - (produto * 5/100)
print(f'O produto valor {produto:.2f}R$ com 5% de desconto temos {desconto:.2f}R$')
