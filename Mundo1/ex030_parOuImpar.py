# Crie um porgrama que leia um número inteiro e mostre na tela se ele é PAR ou ìMPAR
n = int(input('Digite um valor inteiro: '))
if n == 0:
    print('Valor nulo, nem ÌMPAR e nem PAR')
else:
    if n % 2 == 0:
        print(f'{n} é PAR')
    else:
        print(f'{n} é ÍMPAR')
