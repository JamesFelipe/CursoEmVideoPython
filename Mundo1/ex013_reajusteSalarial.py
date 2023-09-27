# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Digite o seu salário: '))
novo_salario = salario + (salario * 15/100)
print(f'Seu salário antigo: {salario:.2f}R$')
print(f'Seu novo salário com 15% de aumenti: {novo_salario}')
