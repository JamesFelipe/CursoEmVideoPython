# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando o laço for

n = int(input('Digite o valor que ver a tabuada: '))
for i in range(1, 11):
    print(f'{n:2} X {i:2} = {i * n:2}')
