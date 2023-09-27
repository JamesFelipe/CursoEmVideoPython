# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

# Para salários superiores a R$1250,00, calcule um aumento de 10%
# Para os inferiores ou iguais o aumento é de 15%
salario = float(input('Digite o seu salário: '))
if salario > 1250:
    aumento_10 = salario + (salario * 10/100)
    print(f'Seu novo salário com 10% de aumento é: {aumento_10:.2f}R$')
else:
    aumento_15 = salario + (salario * 15 /100)
    print(f'Seu novo salário com 15% de aumento é: {aumento_15:.2f}R$')
