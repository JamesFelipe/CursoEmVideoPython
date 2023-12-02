# Crie um programa que leia dois valores e mostre um menu na tela

# [1] somar
# [2] multiplicar
# [3] Maior
# [4] Novos números
# [5] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso
numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''
Selecione o que quer fazer:
[ 1 ] - somar
[ 2 ] - multiplicar
[ 3 ] - Maior
[ 4 ] - Adicionar Novos números
[ 5 ] - sair do programa             
                  
Digite sua opção:  '''))
    print('-' * 30)
    if opcao == 1:
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    elif opcao == 2:
        print(f'{numero1} X {numero2} = {numero1 * numero2}')
    elif opcao == 3:
        if numero1 > numero2:
            print(f'{numero1} é maior que {numero2}')
        else:
            print(f'{numero2} é maior que {numero1}')
    elif opcao == 4:
        numero1 = int(input('Digite o novo valor do 1º valor: '))
        numero2 = int(input('Digite o novo valor do 2º valor: '))
    else:
        print('Valor inválido. Digite uma das opções válidas')